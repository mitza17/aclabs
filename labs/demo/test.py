# not my first app

a = 10
my_string = "aaa"
#print a, my_string

#my_dict = {'test': 10,
#			'abc': [1,2,'test','test2'],
#			'c': dict(a=10),
#			'cd': {'a': 10}
#}
#print my_dict
#print my_dict['abc']
#my_dict['c']='a'
#print dir(my_dict)


#jasdgnsadojgnsdgn
#a=range(10)
#print a[2:-1:2]

# def my_function(a,b,c,d=10):
# 	print locals()

# my_function(1,2, c='test')


# def my_function(a, *args, **kwargs):
# 	print locals()

# my_function(1, 2, 3, kw='test')

# def tuple_example():
# 	my_list=[1,2,3]
# 	my_tuple = (1,2,3)
# 	my_list.append(4)
# 	my_list += [5]
# 	my_tuple2 = 1,
# 	print my_tuple, my_tuple2
# 	print locals()

# tuple_example()

# def func_raising_exception():
# 	raise Exception('expected exception')
# def test_esc():
# 	try:
# 		func_raising_exception()
# 	except (Exception, IOError) as ex:
# 		print ex
# 	finally:
# 		print 'test_exc finished'

# test_esc()


# import contextlib

# @contextlib.contextmanager
# def my_open(*args, **kwargs):
# 	f = None
# 	try:
# 		f = open(*args, **kwargs)
# 		yield f
# 	finally:
# 		if f:
# 			f.close()

# def io_demo():
# 	import os
# 	tmp_file= 'D:\New folder\yolo.txt'
# 	with open(tmp_file,'w') as f:
# 		f.write('test')
# 	with my_open(tmp_file,'r') as f:
# 		print f.read()

# 	os.unlink(tmp_file)

# io_demo()

# def test_xrange():
# 	import pdb
# 	pdb.set_trace()
# 	my_list = xrange(100000)
# 	for i in my_list:
# 		if not (i % 2 == 0):
# 			continue
# 		if (None or '' or 0):
# 			print 'found smth'
# 		print i
# 		if i in range(3):
# 			print '%s < 3' % i
# 		if i == 5:
# 			break
# test_xrange()

# p = (x for x in range(1000000) if (x % 2 == 0))
# print p

# def even_generator():
# 	i = 0
# 	while True:
# 		i += 2
# 		yield i

# for i in even_generator():
# 	print i
# 	if i >=10:
# 		break

# f = lambda x,y,*args,**kwargs: x*y
# print f(1,2,'some other argument')

# def random_func(a,b,c):
# 	return a,b,c

# cbk = lambda: random_func(1,2,3)

# print cbk()

# import functools
# cbk = functools.partial(random_func, 4, 5, 6)
# print cbk()

# def get_callback(f,*args,**kwargs):
# 	def callback():
# 		return f(*args,**kwargs)
# 	return callback

# cbk = get_callback(random_func,7,8,9)
# print cbk()

# import json
# my_dict = dict(key=10)
# serialized = json.encode(my_dict)
# print serialized
# received = json.parse(serialized)
# print received

# my_string = "%(id)s-%(nume)s" % dict(id=0, nume='Anon')
# print my_string