from mysite.apps.news.models import *


User.objects.create_user(full_name = "Иванов Иван Иванович", username='user1')
User.objects.create_user(full_name = "Петров Петр Петрович",  username='user2')
print(User.objects.filter())

Author.objects.create(user=User.objects.filter()[0])
Author.objects.create(user=User.objects.filter()[1])

for c in [1, 2, 3, 4]:
    Category.objects.create(name='Category'+str(c))

Post.objects.create(
        author = Author.objects.filter()[0],
        article = True,
        categories = [Category.objects.filter()[0], Category.objects.filter()[1]],
        title = 'some title 1',
        text = 'Впервые термин «вики» для описания веб-сайта был использован в 1995 году Уордом Каннингемом, разработчиком первой вики-системы WikiWikiWeb, «Портлендского хранилища образцов» программного кода[2], созданной 25 марта 1995 года, который заимствовал слово гавайского языка, означающее «быстрый»[3][4]. Каннингем объяснил выбор названия движка тем, что он вспомнил работника международного аэропорта Гонолулу, посоветовавшего ему воспользоваться вики-вики шаттлом — небольшим автобусом, курсировавшим между терминалами аэропорта. Каннингем же планировал сделать движок, позволявший пользователям максимально быстро редактировать и создавать статьи. Каннингем первоначально описал вики как «простейшую онлайн-базу данных, которая может функционировать»[5]. Позже этому слову был придуман английский бэкроним «What I Know Is…» («то, что я знаю, это…»)[6].',
    )
Post.objects.create(
        author = Author.objects.filter()[1],
        article = True,
        categories = [Category.objects.filter()[2], Category.objects.filter()[1]],
        title = 'some title 2',
        text = 'Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[16] или па́йтон[17]) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[20]. Язык является полностью объектно-ориентированным — всё является объектами[18]. Необычной особенностью языка является выделение блоков кода пробельными отступами[21]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[20]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[18]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как Си или C++[20][18].'
    )
Post.objects.create(
        author = Author.objects.filter()[0],
        article = False,
        categories = [Category.objects.filter()[1], Category.objects.filter()[3]],
        title = 'some title 3',
        text = 'Django (Джанго, [dʒæŋɡoʊ][6]) — свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC[7]. Проект поддерживается организацией Django Software Foundation.'
    )

Comment.objects.create(
        post = Post.objects.filter()[0],
        user = Author.objects.filter()[0],
        text = 'Very good'
    )
Comment.objects.create(
        post = Post.objects.filter()[1],
        user = Author.objects.filter()[0],
        text = 'Very very good'
    )
Comment.objects.create(
        post = Post.objects.filter()[1],
        user = Author.objects.filter()[1],
        text = 'I want you to mother my children!'
    )
Comment.objects.create(
        post = Post.objects.filter()[2],
        user = Author.objects.filter()[1],
        text = 'Not so good:('
    )
Comment.objects.filter()[0].like()
Comment.objects.filter()[1].like()
Comment.objects.filter()[2].like()
Comment.objects.filter()[0].like()
Comment.objects.filter()[1].like()
Comment.objects.filter()[2].like()
Comment.objects.filter()[0].like()
Comment.objects.filter()[0].like()
Comment.objects.filter()[3].dislike()

Post.objects.filter()[0].like()
Post.objects.filter()[1].like()
Post.objects.filter()[2].dislike()

print('username лучшего автора', Author.objects.order_by('-rating')[0].username)
print('_____________________________________________________')

best_art = Post.objects.order_by('-rating')[0]
print('дата лучшей статьи ', best_art.datetime)
print('автор статьи ', User.objects.get(id=best_art.user).username)
print('рейтинг', best_art.rating)
print('title ', best_art.title)
best_art.preview()
for com in Comment.objects.filter(post=best_art):
    print(com.text)
    print(com.datetime)
    print('rating ', com.rating)
    print('____________________')
