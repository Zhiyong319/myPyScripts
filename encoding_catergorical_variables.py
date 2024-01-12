import category_encoders as ce
import pandas as pd

''' Ordinal Endcoding '''
# data
train_df=pd.DataFrame({'Degree':['High school','Masters','Diploma','Bachelors','Bachelors','Masters','Phd','High school','High school']})
train_df

# create object of Ordinal encoding
encoder= ce.OrdinalEncoder(cols=['Degree'],return_df=True,
                           mapping=[{'col':'Degree',
'mapping':{'None':0,'High school':1,'Diploma':2,'Bachelors':3,'Masters':4,'Phd':5}}])

df_train_transformed = encoder.fit_transform(train_df)
df_train_transformed

''' One Hot Encoding '''
# data
data=pd.DataFrame({'City':[
'Delhi','Mumbai','Hydrabad','Chennai','Bangalore','Delhi','Hydrabad','Bangalore','Delhi'
]})

# create object for one-hot encoding
encoder=ce.OneHotEncoder(cols='City',handle_unknown='return_nan',return_df=True,use_cat_names=True)

data_encoded = encoder.fit_transform(data)
data_encoded

''' Dummy Encoding '''
data_encoded=pd.get_dummies(data=data, drop_first=True) # Here using drop_first  argument, we are representing the first label Bangalore using 0.
data_encoded

''' Effect/Sum/Deviation Encoding '''
encoder=ce.sum_coding.SumEncoder(cols='City',verbose=False,)
data_encoded = encoder.fit_transform(data)
data_encoded

''' Binary Encoding '''
encoder= ce.BinaryEncoder(cols=['City'],return_df=True)
data_encoded=encoder.fit_transform(data)
data_encoded

''' Base N Encoding '''
encoder= ce.BaseNEncoder(cols=['City'],return_df=True,base=5)
data_encoded=encoder.fit_transform(data)
data_encoded

''' Target Encoding '''
# data
data=pd.DataFrame({'class':['A,','B','C','B','C','A','A','A'],'Marks':[50,30,70,80,45,97,80,68]})
encoder=ce.TargetEncoder(cols='class')
encoder.fit_transform(data['class'],data['Marks'])

#Create target encoding object
encoder=ce.TargetEncoder(cols='class')

''' Hash Encoding '''
# data
data=pd.DataFrame({'Month':['January','April','March','April','Februay','June','July','June','September']})

#Create object for hash encoder
encoder=ce.HashingEncoder(cols='Month',n_components=6)
encoder.fit_transform(data)
