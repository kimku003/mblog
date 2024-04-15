from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from mblog.forms import CommentForm
from django.shortcuts import render, get_object_or_404

from django.core.mail import send_mail
from django.http import HttpResponse

from .models import ContactInfo, Post, ProfileImage
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class PostList(generic.ListView):
    template_name = "mblog/index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_images"] = ProfileImage.objects.all()
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = "mblog/post_detail.html"


class ProfiilDetail(generic.DetailView):
    model = ProfileImage
    template_name = "mblog/index.html"


def about(request):
    return render(request, "mblog/about.html")


def contact(request):
    return render(request, "mblog/contact.html")


def create_userinfo(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            userinfo = form.save()

            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect("home", userinfo.id)

    else:
        form = ContactForm()

    return render(request, "mblog/create_userinfo.html", {"form": form})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None  # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request,
        "mblog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def info_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Enregistrement des données du formulaire dans la base de données
            contact_info = ContactInfo(
                lastname=form.cleaned_data["lastname"],
                firstname=form.cleaned_data["firstname"],
                birth_day=form.cleaned_data["birth_day"],
                email=form.cleaned_data["email"],
                description=form.cleaned_data["description"],
            )
            contact_info.save()

            # Redirection ou affichage d'un message de succès
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "mblog/info.html", {"form": form})


def like_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        value = request.POST.get("value")
        post = Post.objects.get(id=post_id)
        post.likes += int(value)
        post.save()
        return JsonResponse({"likes": post.likes})
