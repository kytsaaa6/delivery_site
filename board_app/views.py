from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from board_app.forms import BoardForm
from board_app.models import BoardDB
from django.core.paginator import Paginator

# Create your views here.
def boardIndex(request):
    if request.method == 'GET':
        data = BoardDB.objects.all()
        context = {}
    elif request.method == 'POST':
        data = BoardDB.objects.filter(title__contains=request.POST.get('search'))
        context = {}
    paging = Paginator(data, 3)
    page = paging.page(request.GET.get('page',1))
    context.update(
        {
            'data':page,
            'page_range':paging.page_range
        }
    )
    return render(request, 'board_app/index.html',context)

def boardDetail(request, board_id):
    if request.method == 'GET':
        data = BoardDB.objects.get(id=board_id)

        # 게시물 조회시에 조회수를 1 증가시킨다
        data.view_count += 1

        # update_fields 는 튜플 자료형이기 때문에 업데이트할 필드가 하나밖에 없더라도 , 를 입력 해줘야 한다
        data.save(update_fields=('view_count',))

        context = {
            'data': data
        }

        return render(request, 'board_app/detail.html', context)

def boardWrite(request):
    if request.method == 'GET':
        # BoardForm 객체를 보내줄 때 author는 접속한 유저의 이름 값을 애초에 넣어준다
        form = BoardForm(initial={'author': request.user.username})

        context = {
            'form': form
        }

        return render(request, 'board_app/write.html', context)

    elif request.method == 'POST':
        data = BoardDB(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            context=request.POST.get('context')
        )
        data.save()

        # 작성과 동시에 그 게시물의 상세 창(detail.html)으로 넘어간다
        # 상세 창에서 그 게시물의 데이터를 추출하기 위해 data.id(게시물의 id)도 같이 넘김
        # detail의 url 정규 표현식에도 사용된다
        return redirect('detail', data.id)


def boardUpdate(request):
    if request.method == 'GET':

        data = BoardDB.objects.get(id=request.GET.get('id'))

        #if request.user.username == data.author:
        form = BoardForm(
            initial={
                'title': data.title,
                'author': data.author,
                'context': data.context
            }
        )
        context = {
            'data': data,
            'form': form
        }
        return render(request, 'board_app/update.html', context)
    elif request.method == 'POST':

        data = BoardDB.objects.get(id=request.POST.get('id'))

        #if request.user.username == data.author:
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        data.context = request.POST.get('context')
        data.save()

    return redirect('detail', data.id)

def boardDelete(request):
    if request.method == 'GET':

        board_id = request.GET.get('id')

        context = {
            'id': board_id
        }

        return render(request, 'board_app/delete.html', context)

    elif request.method == 'POST':
        data = BoardDB.objects.get(id=request.POST.get('id'))

        data.delete()

        return redirect('index')

def boardGoodBad(request, type):
    if request.method == 'GET':
        data = BoardDB.objects.get(id=request.GET.get('id'))
        if type == 'good':
            data.good_count += 1
        elif type == 'bad':
            data.bad_count += 1

        # 추천 버튼을 누르는 동시에 detail 페이지로 redirect 시켜주기 때문에 조회수도 자동적으로 상승
        # 그렇기 때문에 조회수를 미리 하나 줄인다
        data.view_count -= 1

        # updata_data 필드의 갱신을 막기 위해서 updata_field 를 직접 명시
        data.save(update_fields=('good_count', 'bad_count', 'view_count'))

    return redirect('detail', data.id)

def login(request):
    return render(request, 'registration/login.html')

def join(request):
    if request.method == 'GET':
        return render(request, 'registration/join.html')
    elif request.method == 'POST':
        #가입시에 제출한 username과 중복된 계정이 있는지 확인
        # count()는 object의 수량을 센다
        # data가 0이라면 중복되는 계정이 없다는 뜻
        data = User.objects.filter(username = request.POST.get('username')).count()
        if data == 0:
            if request.POST.get('password') == request.POST.get('password_check'):
                user = User()
                user.username = request.POST.get('username')
                user.set_password(request.POST.get('password'))
                user.email = request.POST.get('email')
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.save()

            else:
                context = dict(request.POST)
                context.update(
                    {
                        'password_error' : '패스워드 불일치'
                    }
                )
                return render(request, 'registration/join.html', context)
        else:
            context = dict(request.POST)
            context.update(
                {
                    'username_error' : '해당 username은 이미 존재 합니다'
                }
            )
        return render(request, 'registration/join.html', context)

    return redirect('/')
