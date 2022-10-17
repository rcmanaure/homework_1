from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user
from services.forms.forms import UpdateAccountForm, ItemForm
from .app import User, db, app, Item
import os
import secrets
from PIL import Image
from flasgger import swag_from

# Init the Blueprints of be used in the mains routes.
main = Blueprint("main", __name__)


def save_picture(form_picture):
    # To save new profile pic.
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@main.route("/profile/delete", methods=["POST", "GET"])
# To delete current logged User.
@login_required  # Must be log in.
def delete_profile():
    user = User.query.filter_by().first()
    if user.id != current_user.id:
        abort(403)
    db.session.delete(user)
    db.session.commit()
    flash("Your account has been deleted!", "success")
    return redirect(url_for("main.publication"))


@main.route("/profile", methods=["GET"])
# Show the items in the home page.
@swag_from("./docs/profile/profile_user.yaml")
def profile_user():
    form = UpdateAccountForm()
    return render_template("profile.html", form=form)


@main.route("/profile", methods=["POST"])
# To update the user account.
@login_required  # Must be log in.
@swag_from("./docs/profile/profile.yaml")
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated.")
        return redirect(url_for("main.profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    photo = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "profile.html", name=current_user.email, photo=photo, form=form
    )


@main.route("/", methods=["GET"])
# Show the Items in the home page.
@swag_from("./docs/publications/posts.yaml")
def publication():
    publications = Item.query.all()
    return render_template("publication.html", publications=publications)


@main.route("/post/new", methods=["POST", "GET"])
# To add a new Item.
@login_required
@swag_from("./docs/publications/post.yaml")
def new_post():
    form = ItemForm()
    if form.validate_on_submit():
        post = Item(
            name=form.name.data,
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id,
            author=current_user.username,
            capacity=form.capacity.data,
            package=form.package.data,
            fridge=form.fridge.data,
            status="CREATED",
        )
        db.session.add(post)
        db.session.commit()
        flash("Your item has been created!", "success")
        return redirect(url_for("main.publication"))
    return render_template("create_post.html", form=form, legend="New Item")


@main.route("/post/<uuid:id>")
# To get a specific Item.
def post(id):
    publication = Item.query.get_or_404(id)
    return render_template("post.html", publication=publication)


@main.route("/post/<uuid:id>/update", methods=["GET", "POST"])
# To update a specific Item.
@login_required
@swag_from("./docs/publications/update_post.yaml")
def update_post(id):
    post = Item.query.get_or_404(id)
    if post.user_id != current_user.id:
        abort(403)
    form = ItemForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.capacity = form.capacity.data
        post.package = form.package.data
        post.fridge = form.fridge.data
        post.name = form.name.data
        post.status = "UPDATED"
        db.session.commit()
        flash("Your item has been updated!", "success")
        return redirect(url_for("main.post", id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
        form.capacity.data = post.capacity
        form.package.data = post.package
        form.fridge.data = post.fridge
        form.name.data = post.name
    return render_template("create_post.html", form=form, legend="Update Item")


@main.route(
    "/post/<uuid:post_id>/delete",
    methods=["POST", "GET"],
)
# To delete a specific Item.
@login_required
@swag_from("./docs/publications/delete_post.yaml")
def delete_post(post_id):
    post = Item.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your item has been deleted!", "success")
    return redirect(url_for("main.publication"))
