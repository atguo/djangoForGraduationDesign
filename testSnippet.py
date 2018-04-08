from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 创建数据
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language': u'python', 'style': u'friendly'}


# 将字典转换成json格式
content = JSONRenderer().render(serializer.data)
content
# '{"id": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false, "language": "python", "style": "friendly"}'
#反序列化是类似的。首先我们将一个流解析成Python支持数据类型。

# 将json转换成字典格式
from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
#然后我们将这些本机数据类型恢复到完全填充的对象实例中

serializer = SnippetSerializer(data=data)
serializer.is_valid()    # 验证数据是否符合要求
# True
serializer.validated_data    # 验证后的数据
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()    # 保存数据
# <Snippet: Snippet object>
