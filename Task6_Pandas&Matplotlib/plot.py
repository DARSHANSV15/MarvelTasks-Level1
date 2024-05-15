import pandas as pd
import matplotlib.pyplot as plt 

data = {'Role':['Data Scientist','Full Stack','Backend','Cloud'],
        'Experience' : [10 , 6 , 8 , 4 ]
}

df = pd.DataFrame(data)

df.plot(x='Role',y='Experience',marker='o',linestyle='-',color='b',legend=False)
plt.title('Experience Graph')
plt.xlabel('Job Role')
plt.ylabel('Experience in Years')
plt.show()

df.plot(x='Role', y='Experience', kind='bar', legend=False)
plt.title('Experience Graph')
plt.xlabel('Job Role')
plt.ylabel('Experience in years')
plt.show()

df.plot(x='Role', y='Experience', kind='scatter', legend=False)
plt.title('Experience Graph')
plt.xlabel('Job Role')
plt.ylabel('Experience in years')
plt.show()