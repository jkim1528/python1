# if문을 사용해서 비교
people = 5
apple = 6
if people == apple:
    print('everyone ok')
if people < apple:
    print('not everyone')

people = 5
banana = 5
if people == banana:
    print('okay')

banana = 4
if people != banana:
    print('not okay')
if not people == banana:
    print('not okay')

people = 3
banana = 3
apple = 4

if people == banana and people == apple:
    print('subete okay')
if people == banana or people == apple:
    print('izureka okay')
