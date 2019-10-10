"""BMSproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import index,zhuce,denglu,exitd,appdept,appproduct,apppversion,appmeans,appmatter,appproject
from app.views import showuser,upuser,showdept,updetp,showproduct,upproduct,banben,fileupload
from app.views import showmeans,wenjiandd,meanswj,showmiaoshu,showproject,upproject,showmatter,jshowmatter
from app.views import upmatter,fenpeimatter,jshowuser,jshowdept,jshowproduct,qshowmatter,qupmatter,xmindex,cpindex,kfindex

from app.views import gerenxinxi,jshowproject,kshowmatter,wenjianxiazai,filexiazai2,tzsucess,goajax,xiangmu,deptselect

from app.views import projectselect,jueseselect,souname


urlpatterns = [
    path('admin/', admin.site.urls),
path('index/', index),
path('zhuce/', zhuce),
path('denglu/', denglu),
path('exitd/', exitd),
path('appdept/', appdept),
path('appproduct/', appproduct),
path('apppversion/', apppversion),
path('appmeans/', appmeans),
path('appmatter/', appmatter),
path('appproject/', appproject),

path('showuser/', showuser),
path('upuser/<int:uid>/', upuser),
path('showdept/', showdept),
path('updept/<int:deptdid>/',updetp),
path('showproduct/', showproduct),
path('upproduct/<int:pid>/',upproduct),
path('banben/', banben),
path('fileupload/', fileupload),
path('showmeans/', showmeans),
path('wenjiandd/', wenjiandd),
path('meanswj/', meanswj),
path('showmiaoshu/<int:mid>/',showmiaoshu),
path('showproject/', showproject),
path('upproject/<int:pid>/',upproject),
path('showmatter/', showmatter),
path('upmatter/<int:mid>/',upmatter),
path('fenpeimatter/<int:mid>/',fenpeimatter),
path('jshowuser/', jshowuser),
path('jshowdept/', jshowdept),
path('jshowproduct/', jshowproduct),
path('qshowmatter/', qshowmatter),
path('qupmatter/<int:mid>/',qupmatter),
path('jshowmatter/', jshowmatter),
path('xmindex/', xmindex),
path('cpindex/', cpindex),
path('kfindex/', kfindex),
path('gerenxinxi/<int:uid>/', gerenxinxi),
path('jshowproject/', jshowproject),
path('kshowmatter/', kshowmatter),
path('wenjianxiazai/', wenjianxiazai),
path('filexiazai2/<str:filename>/', filexiazai2),
path('tzsucess/', tzsucess),
path('goajax/<str:username>/', goajax),
path('xiangmu/', xiangmu),
path('deptselect/<int:deptid>/', deptselect),
path('projectselect/<int:projectid>/', projectselect),
path('jueseselect/<str:juese>/', jueseselect),
path('souname/', souname),


]