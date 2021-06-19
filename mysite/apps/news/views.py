from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import ListView, DetailView
# from .models import Post

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'detail_news.html' # название шаблона будет product.html
    context_object_name = 'post' # название объекта. в нём будет


class Init(ListView):
        # Инициализация бд
        # User.objects.create_user(first_name = "Иванов Иван Иванович", username='user4')
        # User.objects.create_user(first_name = "Петров Петр Петрович",  username='user5')
        # print(User.objects.filter())

        # Author.objects.create(user=User.objects.filter()[0])
        # Author.objects.create(user=User.objects.filter()[1])

        # for c in [1, 2, 3, 4]:
        #     Category.objects.create(name='Category'+str(c))
        # print(Category.objects.filter(id__in=[1,2]).values_list('id', flat=True), '============================================================================')

        # post1 = Post.objects.create(
        #         author = Author.objects.filter()[0],
        #         article = True,
        #         # categories.set() = [Category.objects.filter()[0], Category.objects.filter()[1]],
        #         title = 'some title 1',
        #         text = 'Впервые термин «вики» для описания веб-сайта был использован в 1995 году Уордом Каннингемом, разработчиком первой вики-системы WikiWikiWeb, «Портлендского хранилища образцов» программного кода[2], созданной 25 марта 1995 года, который заимствовал слово гавайского языка, означающее «быстрый»[3][4]. Каннингем объяснил выбор названия движка тем, что он вспомнил работника международного аэропорта Гонолулу, посоветовавшего ему воспользоваться вики-вики шаттлом — небольшим автобусом, курсировавшим между терминалами аэропорта. Каннингем же планировал сделать движок, позволявший пользователям максимально быстро редактировать и создавать статьи. Каннингем первоначально описал вики как «простейшую онлайн-базу данных, которая может функционировать»[5]. Позже этому слову был придуман английский бэкроним «What I Know Is…» («то, что я знаю, это…»)[6].'
        #     )
        # post1.categories.add(1)
        # post1.categories.add(2)
        #
        # post2 = Post.objects.create(
        #         author = Author.objects.filter()[1],
        #         article = True,
        #
        #         title = 'some title 2',
        #         text = 'Python (МФА: [pʌɪθ(ə)n]; в русском языке встречаются названия пито́н[16] или па́йтон[17]) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[20]. Язык является полностью объектно-ориентированным — всё является объектами[18]. Необычной особенностью языка является выделение блоков кода пробельными отступами[21]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[20]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[18]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как Си или C++[20][18].',
        #     )
        # # post2.categories.add(Category.objects.filter(id__in=[1,3]).values_list('id', flat=True))
        # post2.categories.add(1)
        # post2.categories.add(3)
        #
        # post3 = Post.objects.create(
        #         author = Author.objects.filter()[0],
        #         article = False,
        #
        #         # categories.set() = [Category.objects.filter()[1], Category.objects.filter()[3]],
        #         title = 'some title 3',
        #         text = 'Django (Джанго, [dʒæŋɡoʊ][6]) — свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC[7]. Проект поддерживается организацией Django Software Foundation.',
        #     )
        # # post3.categories.add(Category.objects.filter(id__in=[4,2]).values_list('id', flat=True))
        # post3.categories.add(2)
        # post3.categories.add(4)
        #
        # Comment.objects.create(
        #         post = Post.objects.filter()[0],
        #         user = User.objects.filter()[1],
        #         text = 'Very good'
        #     )
        # Comment.objects.create(
        #         post = Post.objects.filter()[1],
        #         user = User.objects.filter()[1],
        #         text = 'Very very good'
        #     )
        # Comment.objects.create(
        #         post = Post.objects.filter()[1],
        #         user = User.objects.filter()[2],
        #         text = 'I want you to mother my children!'
        #     )
        # Comment.objects.create(
        #         post = Post.objects.filter()[2],
        #         user = User.objects.filter()[2],
        #         text = 'Not so good:('
        #     )

        # Comment.objects.filter()[0].like()
        # Comment.objects.filter()[1].like()
        # Comment.objects.filter()[2].like()
        # Comment.objects.filter()[0].like()
        # Comment.objects.filter()[1].like()
        # Comment.objects.filter()[2].like()
        # Comment.objects.filter()[0].like()
        # Comment.objects.filter()[0].like()
        # Comment.objects.filter()[3].dislike()
        #
        # Post.objects.filter()[0].like()
        # Post.objects.filter()[1].like()
        # Post.objects.filter()[2].dislike()
    pass
