gorod={
	'city' : 'Москва',
	'temperature' : '20'
}
print (gorod['city'])
print(gorod['temperature'])
gorod['temperature']=int(gorod['temperature'])-5
print(gorod['temperature'])
print(gorod)
print(gorod.get('country'))
gorod.get('country','Россия')