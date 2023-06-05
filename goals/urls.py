# from django.urls import path
#
# from goals.views import goal_category, goals
#
# urlpatterns = [
#     path("goal_category/create", goal_category.GoalCategoryCreateView.as_view(), name='create_category'),
#     path("goal_category/list", goal_category.GoalCategoryListView.as_view(), name='category_list'),
#     path("goal_category/<int:pk>", goal_category.GoalCategoryDetailView.as_view(), name='category_detail'),
#
#     path("goal/create", goals.GoalCreateView.as_view(), name='create_goal'),
#     path("goal/list", goals.GoalListView.as_view(), name='goal_list'),
#     path("goal/<int:pk>", goals.GoalDetailView.as_view(), name='goal_detail'),
#     ]
from django.urls import path

from goals import views


urlpatterns = [
    path("goal/create", views.GoalCreateView.as_view()),
    path("goal/list", views.GoalListView.as_view()),
    path("goal/<int:pk>", views.GoalView.as_view()),
    path("goal_category/create", views.GoalCategoryCreateView.as_view()),
    path("goal_category/list", views.GoalCategoryListView.as_view()),
    path("goal_category/<int:pk>", views.GoalCategoryView.as_view()),
    path("goal_comment/create", views.GoalCommentCreateView.as_view()),
    path("goal_comment/list", views.GoalCommentListView.as_view()),
    path("goal_comment/<int:pk>", views.GoalCommentView.as_view()),
]