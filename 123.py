
import pandas

df = pandas.read_csv('/home/user/Загрузки/titanic.csv')
print(df.columns)
z = df['Name']
print(len(z))
x = df[df['Sex'] == 'male']
print(len(x))
y = df[df['Survived'] == 1]
print(len(y))
print((342/891) * 100)
b = df[df['Sex'] == 'female']
print(len(b))
a = df[(df['Survived'] == 1) & (df['Sex'] == 'male')]
print(len(a))
print(df.shape)
c = df[(df['Survived'] == 0) & (df['Pclass'] == 3)]
print(len(c))
