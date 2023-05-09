from django.shortcuts import render, redirect
from .models import KnowledgeData
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
# ログインできるユーザの作成
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Contact_Form


def FirstLogin(request):
    # renderとは描画するという意味。
    return render(request, "login-page.html")

def TopPage(request):
    return render(request, "top-page.html")

def KnowledgeList(request):
    model = KnowledgeData
    object_list = model.objects.all()
    return render(request, 'sample-list.html', {'object_list':object_list})
    #return render(request, "knowledge-list.html")

def Create(request):
    form = Contact_Form()
    context = {'form': form}
    return render(request, 'post-sample.html', context)

def Add(request):
   #POST時の処理を記載
   if request.method == "POST":
       userform= Contact_Form(request.POST)
       #フォーム入力が有効な場合
       if userform.is_valid():
           #入力項目をデータベースに保存
           userform.save(commit=True)
   model = KnowledgeData.objects.all()
   return render(request, 'sample-list.html', {'object_list':model})

def Edit(request,pk):
   model = KnowledgeData
   object = model.objects.get(pk=pk)
   form = Contact_Form(instance=object)
   context = {
       'object':object,
       'form':form,
   }
   return render(request, 'edit.html', context)

def UpdateData(request,pk):
    model = KnowledgeData
    if request.method=="POST":
        object = model.objects.get(pk=pk)
        form = Contact_Form(request.POST,instance=object)
        if form.is_valid():
            form.save(commit=True)
    return redirect('List')

def DeleteData(request,pk):
    model = KnowledgeData
    object = model.objects.get(pk=pk)
    object.delete()
    return redirect('List')

def Detail(request,pk):
    model = KnowledgeData
    object = model.objects.get(pk=pk)
    member_list = model._meta.get_field('member').choices
    print(member_list)
    print(len(model._meta.get_field('member').choices))
    print(type(model._meta.get_field('member').choices))
    context = {
       'object':object,
   }
    return render(request, 'detail.html', context)

def MemberList(request):
    model = KnowledgeData
    member_list = model._meta.get_field('member').choices
    mem = []
    # list型にNameを入れて、それをtuple型に変換してrenderする。
    for i in range(len(member_list)):
        print(member_list[i][0])
        mem.append(member_list[i][0])
        mem_tuple = tuple(mem)
    print(mem_tuple)
    mmm = model.objects.filter(member='徳竹')
    print(mmm)
    context = {
       'member':mmm,
   }
    return render(request, 'sample.html', context)


def Login(request):
    if request.method=="POST":
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)
        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ログイン成功後に遷移したいページに遷移
                return redirect('top_page')
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    if request.method=='GET':
        return render(request, 'login.html')
    

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=="POST":
        username = request.POST['username_data']
        passowrd = request.POST['password_data']
        try:
            user = User.objects.create_user(username, '', passowrd)
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザはすでに登録されています。'})
    return render(request, 'signup.html', {})