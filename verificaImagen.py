import cv2 # OpenCV para computer vision
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #Para graficar
#import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
#from sklearn.metrics import accuracy_score,precision_score
from sklearn.model_selection import train_test_split

def verificaImagenI(ImagenName, usuario):
  Ruta_dataset = './Dataset'
  Filas=128
  Columnas=128
  Dataset=np.zeros((25,Filas*Columnas+1))

  for i in range(0,25,1):
    Ruta=Ruta_dataset + '/' + str(i+1) + '.jpg'
    img=cv2.imread(Ruta)
    I_gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    I_gris=cv2.resize(I_gris, (Filas,Columnas), interpolation = cv2.INTER_AREA)
    Dataset[i,0:Filas*Columnas]=I_gris.reshape((1,Filas*Columnas))
    if i>=0 and i<=4:
      Dataset[i,Filas*Columnas]=1
    else:
      if i>=5 and i<=9:
        Dataset[i,Filas*Columnas]=2
      else:
        if i>=10 and i<=14:
          Dataset[i,Filas*Columnas]=3
        else:
          if i>=15 and i<=19:
            Dataset[i,Filas*Columnas]=4
          else:
            if i>=20 and i<=24:
              Dataset[i,Filas*Columnas]=5


  #2. Dividing dataset into input (X) and output (Y) variables
  X = Dataset[:,0:Filas*Columnas]
  Y = Dataset[:,Filas*Columnas]

  X_train, X_test,Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=14541)

  # Showing the dataset images
  Index=5
  Imagen=X_train[Index,:]
  Imagen=Imagen.reshape((Filas,Columnas))

  # Data normalization
  scaler = MinMaxScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)

  #5. Evaluando casos mediante todos los clasificadores

  Modelo_0 = KNeighborsClassifier(3)
  Modelo_0.fit(X_train, Y_train)
  Y_pred_0 =Modelo_0.predict (X_test)
  #print("Accuracy KNN",accuracy_score(Y_test, Y_pred_0))

  Modelo_1 = GaussianNB()
  Modelo_1.fit(X_train, Y_train)
  Y_pred =Modelo_1.predict (X_test)
  #print("Accuracy Bayes",accuracy_score(Y_test, Y_pred))

  Modelo_2 = LinearDiscriminantAnalysis()
  Modelo_2.fit(X_train, Y_train)
  Y_pred_2 =Modelo_2.predict (X_test)
  #print("Accuracy LDA",accuracy_score(Y_test, Y_pred_2))

  Modelo_3 = QuadraticDiscriminantAnalysis()
  Modelo_3.fit(X_train, Y_train)
  Y_pred_3 =Modelo_3.predict (X_test)
  #print("Accuracy QDA",accuracy_score(Y_test, Y_pred_3))

  Modelo_4 = DecisionTreeClassifier()
  Modelo_4.fit(X_train, Y_train)
  Y_pred_4 =Modelo_4.predict (X_test)
  #print("Accuracy Tree",accuracy_score(Y_test, Y_pred_4))

  Modelo_5 = SVC()
  Modelo_5.fit(X_train, Y_train)
  Y_pred_5 =Modelo_5.predict (X_test)
  #print("Accuracy SVM",accuracy_score(Y_test, Y_pred_5))

  #Reviewing an specific dataset target
  Test=3
  Target=np.zeros((1,Filas*Columnas))
  Target[0,:]=X_test[Test,:]
  Target_im=Target[0,:].reshape((Filas,Columnas))*255
  plt.imshow(Target_im.astype('uint8'),cmap='gray',vmin=0, vmax=255)
  Prediction_0 =Modelo_0.predict (Target)
  Prediction_1 =Modelo_1.predict (Target)
  Prediction_2 =Modelo_2.predict (Target)
  Prediction_3 =Modelo_3.predict (Target)
  Prediction_4 =Modelo_4.predict (Target)
  Prediction_5 =Modelo_5.predict (Target)
  print("La predicción de KNN es:",Prediction_0,', y debería ser: ',Y_test[Test])
  print("La predicción de Bayes es:",Prediction_1,', y debería ser: ',Y_test[Test])
  print("La predicción de LDA es:",Prediction_2,', y debería ser: ',Y_test[Test])
  print("La predicción de QDA es:",Prediction_3,', y debería ser: ',Y_test[Test])
  print("La predicción de Tree es:",Prediction_4,', y debería ser: ',Y_test[Test])
  print("La predicción de SVM es:",Prediction_5,', y debería ser: ',Y_test[Test])



  #Cargando datos rostros Pascual
  Ruta_dataset = './Dataset_val'
  Test=ImagenName
  Ruta=Ruta_dataset + '/' + str(Test) #+ '.jpg'
  img=cv2.imread(Ruta)
  Filas=128
  Columnas=128
  Target=np.zeros((1,Filas*Columnas))
  I_gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  I_gris=cv2.resize(I_gris, (Filas,Columnas), interpolation = cv2.INTER_AREA)
  Target[0,0:Filas*Columnas]=I_gris.reshape((1,Filas*Columnas))
  Target = scaler.transform(Target)
  Prediction_0 =Modelo_0.predict (Target)
  if Prediction_0==1 and usuario == "edwin":
    return "Edwin"
  if Prediction_0==2 and usuario == "laura" :
    return "Laura"
  if Prediction_0==3 and usuario == "sofia":
    return "Sofia"
  if Prediction_0==4 and usuario == "gabriela":
    return "Gabriela"
  if Prediction_0==5 and usuario == "sol":
    return "Sol"
  return "No hay similitud"
