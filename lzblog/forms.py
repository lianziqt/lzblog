# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, URL
from flask_pagedown.fields import PageDownField
from lzblog.models import Category

class LoginForm(FlaskForm):
    username = StringField('用户名|Username', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('密码|Password', validators=[DataRequired(), Length(1, 64)])
    remember = BooleanField('记住我？|Remember Me ?')
    submit = SubmitField('登陆|Log in')

class SettingForm(FlaskForm):
    name = StringField('名称|Name', validators=[DataRequired(), Length(1,32)])
    blog_title = StringField('博客名|Blog Title', validators=[DataRequired(), Length(1,32)])
    blog_sub_title = StringField('博客子名|Blog Sub Title',validators=[DataRequired(), Length(1,128)] )
    about = PageDownField('关于我|About Page', validators=[DataRequired()])
    submit = SubmitField('提交|Submit')

class PostForm(FlaskForm):
    title = StringField('标题|Title', validators=[DataRequired(), Length(1, 60)])
    category = SelectField('类别|Category', coerce=int, default=1)
    summary = PageDownField('简介|Summary', validators=[DataRequired()])
    body = PageDownField('正文|Body', validators=[DataRequired()])
    submit = SubmitField('提交|Submit')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) 
                                for category in Category.query.order_by(Category.name).all()]

class CategoryForm(FlaskForm):
    name = StringField('类别|Name', validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField('提交|Submit')

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('类别已存在|Name already in use.')

class CommentForm(FlaskForm):
    author = StringField('作者|Name', validators=[DataRequired(), Length(1, 30)])
    email = StringField('电子邮箱|Email', validators=[DataRequired(), Email(), Length(1, 254)])
    site = StringField('个人网页|Site', validators=[Optional(), URL(), Length(0, 255)])
    body = TextAreaField('评论|Comment', validators=[DataRequired()])
    submit = SubmitField('提交|Submit')

class AdminCommentForm(CommentForm):
    author = HiddenField()
    email = HiddenField()
    site = HiddenField()


class LinkForm(FlaskForm):
    name = StringField('链接名称|Name', validators=[DataRequired(), Length(1, 30)])
    url = StringField('URL', validators=[DataRequired(), URL(), Length(1, 255)])
    submit = SubmitField('提交|Submit')