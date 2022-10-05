from news.models import *

ilya = User.objects.create_user(username='Илья', first_name='Илья', last_name='Муромец')
dobrinya = User.objects.create_user(username='Добрыня', first_name='Добрыня', last_name='Никитич')

author1 = Author.objects.create(user=ilya)
author2 = Author.objects.create(user=dobrinya)

Category.objects.create(category_name='Авто')
Category.objects.create(category_name='Еда')
Category.objects.create(category_name='Технологии')
Category.objects.create(category_name='Космос')

post1 = Post.objects.create(post_type='post', title='Новый Volkswagen Golf', text='', author=author1)
post1.text = 'Компания Volkswagen представила новый Volkswagen Golf. Речь идёт о юбилейной спецверсии хетчбэка Volkswagen Golf R 20 Years, которая посвящена 20-летию модели. Эта версия будет выпускаться всего один год и обязательно будет цениться у коллекционеров.'
post2 = Post.objects.create(post_type='post', title='Открыта новая экзопланета',
                            text='JWST открыл новую экзопланету транзитным методом', author=author2)
news1 = Post.objects.create(post_type='post', title='Новшество молекулярной кухни',
                            text='Известный повар поделился свои новым способом приготовления так называемых наносухариков',
                            author=author2)

post1.category.add(Category.objects.get(category_name='Авто'))
post1.category.add(Category.objects.get(category_name='Технологии'))
post2.category.add(Category.objects.get(category_name='Технологии'))
post2.category.add(Category.objects.get(category_name='Космос'))
news1.category.add(Category.objects.get(category_name='Еда'))
news1.category.add(Category.objects.get(category_name='Технологии'))

com1 = Comment.objects.create(text='Интересненько!', post=post1, user=dobrinya)
com2 = Comment.objects.create(text='Ничего удивительного, проходили уже', post=news1, user=dobrinya)
com3 = Comment.objects.create(text='Ого! Я бы попробовал!', post=news1, user=ilya)
com4 = Comment.objects.create(text='Как всегда ничего интересного... Отписываюсь', post=post2, user=ilya)
com5 = Comment.objects.create(text='Как-то дороговато...', post=post1, user=dobrinya)
com6 = Comment.objects.create(text='Я бы купил!', post=post1, user=dobrinya)

post1.like()
post1.like()
post1.like()
post1.like()
post1.like()
post1.dislike()
post2.like()
post2.like()
news1.like()
com1.like()
com2.like()
com2.like()

author1.update_rating()
author2.update_rating()

print('Лучший рейтинг:')
f'{Author.objects.all().order_by("-rating")[0].user.username} - {Author.objects.all().order_by("-rating")[0].rating}'

best_post = Post.objects.all().order_by("-post_rating")[0]
f'дата лобавления: {best_post.time_creation}'
f'username автора: {best_post.author.user.username}'
f'рейтинг: {best_post.post_rating}'
f'заголовок: {best_post.title}'
f'превью: {best_post.preview()}'

comments = Comment.objects.filter(post=best_post).values('text', 'user__username', 'comment_rating', 'time_creation')
for com in comments: print(com['text'], '\n', 'Автор: ', com['user__username'], '\n', 'дата: ', com['time_creation'],
                           '\n', 'рейтинг:', com['comment_rating'], '\n')

