from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

#======================LIST VIEW========================
def list(request):
	return render(request,'newsBlog/files/listBlog.html',{'nav':'common/nav.html','posts':Post.published.all(),'css':'newsBlog/files/listBlogCss.html','js':'newsBlog/files/listBlogJs.html'})
#====================END LIST VIEW=======================




#======================DETAIL VIEW========================
def detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year,publish__month=month, publish__day=day,)

	comments = post.comments.filter(active=True)
	

	return render(request,'newsBlog/files/detailBlog.html',{'nav':'common/nav.html','css':'newsBlog/files/detailBlogCss.html','post':post,'comments':comments,'js':'newsBlog/files/detailBlogJs.html',})
#====================END DETAIL VIEW=======================




@login_required
@require_POST
def comment(request):
	post = get_object_or_404(Post, slug=request.POST.get('slug'), status='published', publish__year=request.POST.get('year'),publish__month=request.POST.get('month'), publish__day=request.POST.get('day'))
	newComment = request.POST.get('newComment')
	newCommentModel = Comment()
	newCommentModel.post = post
	newCommentModel.name = request.user.first_name
	newCommentModel.username = request.user.username
	newCommentModel.body = newComment
	newCommentModel.save()
	return JsonResponse({'status':'ok'})


@login_required
@require_POST
def deletePost(request):
    post = Post.objects.filter(author=request.user,id=request.POST.get("id"))
    post.delete()
    return JsonResponse({'status':'ok'})