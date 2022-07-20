#!/usr/bin/env python
# coding: utf-8

# **Verano de la ciencia 2022** 
# 
# **Universidad de Guanajuato**
# 
# **Proyecto: ¡Fotografía de un agujero negro!**
# 
# 
# Equipo:
# *   Fátima Pamela López Salcedo
# *   Martha Nava Hernández 
# *   Gustavo Andres Concha Valdez

# *Introducción*
# 
# La atención de las personas volvió a centrarse en los agujeros negros en abril de 2019, cuando, por medio del Event Horizon Telescope (EHT), se publicó la primera imagen de la sombra correspondiente a uno de estos objetos en el centro de la galaxia vecina M87*.
# 
# <img src= https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg/480px-Black_hole_-_Messier_87_crop_max_res.jpg width="200">
# 
# Recientemente, en mayo del 2022 se reveló la sombra del agujero negro en el centro de nuestra propia galaxia, Sagitario A*. 
# 
# <img src= https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/EHT_Saggitarius_A_black_hole.tif/lossy-page1-1200px-EHT_Saggitarius_A_black_hole.tif.jpg width="200" >
# 
# La obtención de estas conocidas capturas es fruto en una verdadera proeza científica y tecnológica. No solo fortalece la confianza en el quehacer investigativo, sino que abre las puertas a la consolidación de una cultura científica en la población.
# 
# Al hablar de un agujero negro a la mayoría de las personas se les viene a la mente una esfera completamente negra, capaz de atraer todo a su alrededor y engullirlo sin dejar rastro: una cárcel gravitacional absoluta. La idea, que el día de hoy se respalda en evidencia visual, puede pulirse haciendo una revisión de lo que las matemáticas predicen que es susceptible de observarse: la sombra del agujero negro.
# 
# Para una mayor rigurosidad en la descripción de estos fascinantes objetos es imperativo recurrir a las herramientas matemáticas que permiten su caracterización. En el presente informe se busca describir teóricamente la observación de un agujero negro, como también plantear un programa capaz de dibujar su sombra en función de las cantidades que lo determinan.

# #Marco teórico
# ##¿Qué es y qué caracteriza a un agujero negro?
# 
# Se trata de una región finita del espacio-tiempo en donde se concentra una gran cantidad de masa, la cual genera un campo gravitatorio tan descomunalmente grande que no existe nada capaz de escapar de él, ni siquiera la luz. El concepto de agujero negro es resultado de una de las primeras soluciones a las ecuaciones de campo de la teoría de la relatividad general de A. Einsten, hallada por el físico alemán Karl Schwarzschild.
# 
# Por otro lado, los agujeros negros pueden ser clasificados gracias al teorema de No-Pelo. Este teorema establece que un agujero negro queda completamente caracterizado por únicamente tres parámetros: masa, momento angular y carga eléctrica/magnética. Así, aquel que solo posee masa es conocido como agujero negro de Schwarzschild; es el modelo más sencillo. Un agujero negro de Kerr posee masa y momento angular. Si tiene masa, momento angular y carga eléctrica, se trata de un agujero negro de Kerr-Newman. Aunque en este trabajo no se detallará el caso, existe también el agujero negro de Reissner-Nordström, con masa y carga eléctrica. En el trabajo se desarrollará un modelo adicional, conocido como Bardeen-rotante, que es producto de una masa rotante y carga magnética. 
# 
# Es importante mencionar ciertas partes que componen un agujero negro y que serán relevantes para el trabajo. Posee un disco de acreción, que se trata de un conjunto de gas y polvo a altísimas temperaturas que orbita al objeto. Existe también la esfera de luz, que es aquella región a partir de la cual la luz ya no es capaz de escapar de la atracción gravitacional, marcando así la llamada sombra del agujero negro. La siguiente capa se trata del horizonte de eventos, a partir del cual no es posible escapar, ni siquiera acelerando. Esta región determina un punto de no retorno.
# 
# ##Análisis matemático
# 
# ####Métrica de Schwarzschild
# 
# La métrica de Schwarzschild es la primera solución exacta hallada para las ecuaciones de campo de Einstein. Se trata de una solución estática y con simetría esférica que describe el campo gravitatorio alrededor de una concentración de masa dados una carga eléctrica y momento angular nulos. 
# 
# Si se trabaja con unidades tales que $c=1$, la solución de Schwarzschild para una masa $M$ se resume en el elemento de línea
# \begin{equation}
#  ds^{2}=\left(1- \frac{r_S}{r}\right)dt^{2}-\left(1- \frac{r_S}{r}\right)^{-1}dr^{2}-r^{2}\left(d\theta^{2}+sen^{2}\theta d\phi^{2}\right),
# \end{equation}
# en donde el radio de Schwarzschild está dado por $r_S=2GM$, siendo $G$ la constante de Newton. Puesto que el tamaño de un agujero negro depende del contenido que ha absorbido, cuanto mayor es la masa del agujero negro, mayor es el radio de Schwarzschild. Es precisamente este radio el que determina el horizonte de eventos.
# 
# ###Singularidad
# Existen dos puntos de interés en la métrica de Schwarzschild, que aparentan acarrear problemas en las definiciones. Uno de ellos es $r=r_S$, para el cual
# \begin{equation}
#   \left(1- \frac{r_S}{r}\right)\longrightarrow 0~, ~~~~~~~~ \left(1- \frac{r_S}{r}\right)^{-1}\longrightarrow \infty.
# \end{equation}
# Aunque tal comportamiento parece implicar consecuencias físicas, mediante un cambio de coordenadas adecuado es posible demostrar que este valor no implica una singularidad. Sin embargo, sí es posible hacer un análisis de este punto: una vez que se cruza dicho valor, en la región $r< r_S$, la parte temporal es negativa, mientras que la parte radial, positiva. Esto se describe con cierta frecuencia como un intercambio entre los roles que juegan tiempo y espacio.
# 
# Por otro lado, el punto $r=0$, para el cual
# \begin{equation}
#   \left(1- \frac{r_S}{r}\right)\longrightarrow \infty~, ~~~~~~~~ \left(1- \frac{r_S}{r}\right)^{-1}\longrightarrow 0,
# \end{equation}
# sí representa una singularidad física. Lo que sucede en dicho punto suele describirse como una curvatura hasta el infinito de tiempo y espacio, aunque se trata de especulación: realmente, no está del todo claro qué ocurre en la singularidad.
# 
# ###La sombra de un agujero negro con una métrica más general
# El campo gravitacional de un agujero negro es capaz de desviar la luz que pasa a su alrededor. Dependiendo de las características del objeto, esta luz "doblada" producirá una sombra particular, la cual se capta desde la Tierra, gracias al EHT. Es necesario modelar al observador en un espacio asintóticamente plano, en tanto se encuentra en una región lo suficientemente lejana del agujero negro. Para esto, resulta conveniente definir las llamadas coordenadas celestes, $\alpha$ y $\beta$.
# 
# Veamos cómo se traduce esto en lenguaje matemático. Se recurre a la métrica general
# \begin{equation}
#   ds^2=\frac{a^2\sin^2\theta}{\rho^2}\left(dt^2-\frac{r^2+a^2}{a}d\phi\right)^2+\frac{\rho^2}{Q}dr^2+\rho^2d\theta^2-\frac{Q}{\rho}\left(dt-a\sin^2\theta d\phi\right)^2,
# \end{equation}
# en donde $a=J/M$ es un término asociado al momento angular del agujero negro rotante y $\rho$ se expresa como
# \begin{equation}
#   \rho=r^2+a^2\cos^2\theta,
# \end{equation}
# con $M$ la masa del agujero negro.
# 
# La definición de $Q$ determinará los distintos tipos de agujero negro:
# - Kerr: caraterizado por poseer masa y momento angular
#   \begin{equation}
#     Q=r^2-2Mr+a^2
#   \end{equation}
# 
# - Kerr-Newman: posee masa, momento angular y carga eléctrica
#   \begin{equation}
#     Q=r^2-2Mr+a^2+q^2
#   \end{equation}
# 
# - Bardeen-rotante: posee masa, momento angular y carga magnética
#   \begin{equation}
#     Q=r^2+a^2-\frac{2Mr^4}{(r^2+g^2)^{3/2}}
#   \end{equation}
# 
# Desde luego, si el agujero negro no tiene rotación, al $a=0$ se recupera la solución estática de Schwarzschild.
# 
# ###Ecuaciones geodésicas
# Para el caso general, es necesario tener en cuenta que las componentes inversas de la métrica se forman según
# \begin{equation}
#   g^{tt}=-\frac{1}{\rho^2Q}\left[(r^2+a^2)^2-a^2Q\sin^2\theta\right]
# \end{equation}
# \begin{equation}
#   g^{rr}=\frac{Q}{\rho^2}
# \end{equation}
# \begin{equation}
#   g^{\theta\theta}=\frac{1}{\rho^2}
# \end{equation}
# \begin{equation}
#   g^{\phi\phi}=\frac{Q-a^2\sin^2\theta}{\rho^2Q\sin^2\theta}
# \end{equation}
# \begin{equation}
#   g^{t\phi}=\frac{a}{\rho^2Q}\left[Q-(r^2+a^2)\right]
# \end{equation}
# 
# Luego, con ayuda de la ecuación de Hamilton-Jacobi se puede obtener las ecuaciones geodésicas:
# 
# \begin{equation}
#   \rho^2\dot{t}=\frac{1}{Q}\left\{\left[(r^2+a^2)^2-a^2Q\sin^2\theta\right]E+a\left[Q-(r^2+a^2)\right]L_z\right\},
# \end{equation}
# \begin{equation}
#   \rho^2\dot{\phi}=\frac{1}{Q}\left\{\frac{Q-a^2\sin^2\theta}{\sin^2\theta}L_z-a\left[Q-(r^2+a^2)\right]E\right\},
# \end{equation}
# \begin{equation}
#   \rho^2\dot{r}=\sqrt{\mathcal{R}(r)},
# \end{equation}
# \begin{equation}
#   \rho^2\dot{\theta}=\sqrt{\Theta(\theta)},
# \end{equation}
# en donde $L_z$ es la componente $z$ del momento angular y las funciones $\mathcal{R}(r)$ y $\Theta(\theta)$ se definen como
# \begin{equation}
#   \mathcal{R}(r)=\left[(r^2+a^2)E-aL_z\right]^2-Q\left[m^2r^2+\mathcal{K}+(L_z-aE)^2\right]
# \end{equation}
# \begin{equation}
#   \Theta(r)=\mathcal{K}\cos^2\theta\left[(E^2-m^2)a^2-L_z^2\csc^2\theta\right]
# \end{equation}
# 
# ###Geodésicas nulas: trayectoria de la luz
# Ya que el interés radica en la imagen generada por la observación del agujero negro en cuestión, el análisis se debe centrar en las caraterísticas que tiene la propagación de la luz. Como es sabido, la luz viaja siguiendo geodésicas nulas. Las ecuaciones de movimiento para un haz luminoso pueden determinarse haciendo uso nuevamente de las ecuaciones de Hamilton-Jacobi, considerando que $m=0$ sería lo correspondiente a un fotón luminoso.
# 
# Haciendo $m=0$, $\xi=L_z/E$, $\eta=\mathcal{K}/E^2$ y cambiando el parámetro de la curva por $\lambda_*=E\lambda$, se tiene que
# 
# \begin{equation}
#   \rho^2\dot{t}=\frac{1}{Q}\left[(r^2+a^2)^2-a^2Q\sin^2\theta+a\left(Q-r^2-a^2\right)\xi\right],
# \end{equation}
# \begin{equation}
#   \rho^2\dot{\phi}=\frac{1}{Q}\left[\frac{Q-a^2\sin^2\theta}{\sin^2\theta}\xi-a\left(Q-r^2-a^2\right)\right],
# \end{equation}
# \begin{equation}
#   \rho^2\dot{r}=\sqrt{\mathcal{R}(r)},
# \end{equation}
# \begin{equation}
#   \rho^2\dot{\theta}=\sqrt{\Theta(\theta)},
# \end{equation}
# en donde
# \begin{equation}
#   \mathcal{R}(r)=\left(r^2+a^2-a\xi\right)^2-Q\left[\eta+(\xi-a)^2\right]
# \end{equation}
# \begin{equation}
#   \Theta(r)=\eta+\cos^2\theta\left(a^2-\xi^2\csc^2\theta\right)
# \end{equation}
# 
# Las órbitas que son de interés son las de equilibrio inestable, es decir, las que delimitan un valor de la coordenada radial tal que un fotón describe varias vueltas alrededor del agujero negro, para luego ser capturado o expulsado hacia el infinito. Ya que la expresión $\mathcal{R}=0$ determina los puntos de retorno en la trayectoria de los fotones, para hallar tal órbita basta con buscar las soluciones de
# 
# \begin{equation}
#   \mathcal{R}=\frac{d\mathcal{R}}{dr}=0
# \end{equation}
# 
# Este sistema da como resultado los valores de interés para $\xi$ y $\eta$, dados a continuación:
# 
# \begin{equation}
#   \xi=\frac{(r^2+a^2)Q'-4Qr}{aQ'}
# \end{equation}
# \begin{equation}
#   \eta=\frac{r^2\left[16Q(a^2-Q)+8QQ'r-Q'^2r^2\right]}{a^2Q'^2}
# \end{equation}
# 
# Como se mecionaba, la forma más práctica de representar la sombra del agujero negro viene dada por el uso de las coordenadas celestes $\alpha$ y $\beta$. Considerando a un observador ubicado en un espacio asintóticamente plano, en $(r_0,\theta_0,0)$, estas coordenadas se definen como
# \begin{equation}
#   \alpha=\lim_{r_0\rightarrow\infty}\left(-r_0^2\sin\theta_0\frac{d\phi}{dr}\right)
# \end{equation}
# \begin{equation}
#   \beta=\lim_{r_0\rightarrow\infty}r_0^2\frac{d\theta}{dr}
# \end{equation}
# 
# Si se utiliza las relaciones anteriormente escritas, las coordenadas celestes quedan dadas por
# \begin{equation}
#   \alpha=-\frac{\xi}{\sin\theta_0}
# \end{equation}
# \begin{equation}
#   \beta=\pm\sqrt{\eta+a^2\cos^2\theta_0-\xi^2\cot^2\theta_0}
# \end{equation}
# Los fotones que son capaces de llegar al observador son aquellos para los cuales $\beta$ queda bien definido. En ese sentido, los valores permitidos para la coordenada radial quedan determinados por el intervalo entre las raíces de la ecuación $\beta^2=0$.
# 
# En el presente trabajo se busca modelar un observador ubicado en $\theta_0=\pi/2$. Con esto establecido, la ecuación que determinará el intervalo de valores de $r$ es
# \begin{equation}
#   \beta^2=\eta=0.
# \end{equation}
# Por lo tanto, tomando en cuenta la expresión que define $\eta$, la ecuación de interés resulta ser
# \begin{equation}
#   16Q(a^2-Q)+8QQ'r-Q'^2r^2=0.
# \end{equation}
# 
# El programa que se planteará en este informe busca resolver numéricamente la ecuación mostrada. Una vez determinados los valores que puede asumir $r$, se procede a dibujar la sombra del agujero negro en un gráfico de $\alpha$ vs $\beta$.
# 
# ###Consideraciones adicionales
# Es necesario garantizar que los valores que asuma la dimensión radial queden fuera del horizonte de eventos, de lo contrario se estaría entrando en contradicción. A continuación el horizonte de eventos para distintos valores de $a$ para los casos de Kerr ($M=1$) y Kerr-Newman ($M=1$, $q=0.5$):
# 
# ![picture](https://drive.google.com/uc?id=1y_2UzBQmbIVRmFscYODuz5c4wg9AgFXx)
# 

# ***Código para obtener la sombra del agujero negro***

# En esta primera parte se importan las librerías necesarias para la ejecución del programa:
# 

# In[9]:


import numpy as np
from matplotlib import pyplot as plt


# #Kerr
# Se hará variaciones en el momento angular. Ya que se desea tener las raíces, se grafica $16Q(a^2-Q)+8QQ'r-Q'^2r^2$ para encontrar los valores límite de r.
# 
# 
# ![picture](https://drive.google.com/uc?id=1prEtIq4yjo8EqErVGndZVftx4OeDg291)
# 

# 

# Se comienza definiendo el valor de la masa $M$, el valor de $a$, asociado a la rotación del cuerpo, y el ángulo $\theta$ con que se observa, que en adelante será siempre ecuatorial, como se había indicado. Los valores para la masa y el ángulo se mantendrán a lo largo del documento.

# In[10]:


M=1
theta=np.pi/2


# Se dividirá el código en varias partes, de manera que se pueda variar el parámetro $a$. Además, recurrentemente se utiliza la función HallarRaices(A,B,nmax,tolerancia), la cual se trata de un método numérico para hallar raíces reales de funciones. Se usa el conocido método de la secante para tal fin. La función denominada anul(r) es, precisamente,
# \begin{equation}
#   anul(r)=16Q(a^2-Q)+8QQ'r-Q'^2r^2,
# \end{equation}
# que tendrá diferentes formas dependiendo del tipo de agujero negro (que determina $Q$).

# In[19]:


a1=0.1

def anul1(r):
  Q=r**2-2*M*r+a1**2
  Qp=2*r-2*M
  return 16*Q*(a1**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices1(A,B,nmax,tolerancia):
  fA=anul1(A)
  fB=anul1(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul1(A)
    if abs(d)<tolerancia:
      break
  return A

rInic1=HallarRaices1(2.8,2.9,1000,0.0000001)
rFin1=HallarRaices1(3.1,3.2,1000,0.0000001)

def alfa1(r):
  Q=r**2-2*M*r+a1**2
  Qp=2*r-2*M
  xi=((a1**2+r**2)*Qp-4*r*Q)/(a1*Qp)
  return -xi/np.sin(theta)

def beta1(r):
  Q=r**2-2*M*r+a1**2
  Qp=2*r-2*M
  xi=((a1**2+r**2)*Qp-4*r*Q)/(a1*Qp)
  eta=(r**2/(a1**2*Qp**2))*(anul1(r))
  return np.sqrt(eta+a1**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[21]:


a2=0.25

def anul2(r):
  Q=r**2-2*M*r+a2**2
  Qp=2*r-2*M
  return 16*Q*(a2**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices2(A,B,nmax,tolerancia):
  fA=anul2(A)
  fB=anul2(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul2(A)
    if abs(d)<tolerancia:
      break
  return A

rInic2=HallarRaices2(2.6,2.8,1000,0.0000001)
rFin2=HallarRaices2(3.2,3.4,1000,0.0000001)

def alfa2(r):
  Q=r**2-2*M*r+a2**2
  Qp=2*r-2*M
  xi=((a2**2+r**2)*Qp-4*r*Q)/(a2*Qp)
  return -xi/np.sin(theta)

def beta2(r):
  Q=r**2-2*M*r+a2**2
  Qp=2*r-2*M
  xi=((a2**2+r**2)*Qp-4*r*Q)/(a2*Qp)
  eta=(r**2/(a2**2*Qp**2))*(anul2(r))
  return np.sqrt(eta+a2**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[12]:


a3=0.5

def anul3(r):
  Q=r**2-2*M*r+a3**2
  Qp=2*r-2*M
  return 16*Q*(a3**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices3(A,B,nmax,tolerancia):
  fA=anul3(A)
  fB=anul3(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul3(A)
    if abs(d)<tolerancia:
      break
  return A

rInic3=HallarRaices3(2.3,2.4,1000,0.0000001)
rFin3=HallarRaices3(3.4,3.6,1000,0.0000001)

def alfa3(r):
  Q=r**2-2*M*r+a3**2
  Qp=2*r-2*M
  xi=((a3**2+r**2)*Qp-4*r*Q)/(a3*Qp)
  return -xi/np.sin(theta)

def beta3(r):
  Q=r**2-2*M*r+a3**2
  Qp=2*r-2*M
  xi=((a3**2+r**2)*Qp-4*r*Q)/(a3*Qp)
  eta=(r**2/(a3**2*Qp**2))*(anul3(r))
  return np.sqrt(eta+a3**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[14]:


a4=0.75

def anul4(r):
  Q=r**2-2*M*r+a4**2
  Qp=2*r-2*M
  return 16*Q*(a4**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices4(A,B,nmax,tolerancia):
  fA=anul4(A)
  fB=anul4(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul4(A)
    if abs(d)<tolerancia:
      break
  return A

rInic4=HallarRaices4(1.8,2.0,1000,0.0000001)
rFin4=HallarRaices4(3.6,4.0,1000,0.0000001)

def alfa4(r):
  Q=r**2-2*M*r+a4**2
  Qp=2*r-2*M
  xi=((a4**2+r**2)*Qp-4*r*Q)/(a4*Qp)
  return -xi/np.sin(theta)

def beta4(r):
  Q=r**2-2*M*r+a4**2
  Qp=2*r-2*M
  xi=((a4**2+r**2)*Qp-4*r*Q)/(a4*Qp)
  eta=(r**2/(a4**2*Qp**2))*(anul4(r))
  return np.sqrt(eta+a4**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[17]:


a5=0.9

def anul5(r):
  Q=r**2-2*M*r+a5**2
  Qp=2*r-2*M
  return 16*Q*(a5**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices5(A,B,nmax,tolerancia):
  fA=anul5(A)
  fB=anul5(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul5(A)
    if abs(d)<tolerancia:
      break
  return A

rInic5=HallarRaices5(1.4,2.0,1000,0.0000001)
rFin5=HallarRaices5(3.5,4.1,1000,0.0000001)

def alfa5(r):
  Q=r**2-2*M*r+a5**2
  Qp=2*r-2*M
  xi=((a5**2+r**2)*Qp-4*r*Q)/(a5*Qp)
  return -xi/np.sin(theta)

def beta5(r):
  Q=r**2-2*M*r+a5**2
  Qp=2*r-2*M
  xi=((a5**2+r**2)*Qp-4*r*Q)/(a5*Qp)
  eta=(r**2/(a5**2*Qp**2))*(anul5(r))
  return np.sqrt(eta+a5**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# Ya con estas cantidades, es posible configurar el gráfico a realizarse:

# In[22]:


r1=np.linspace(rInic1,rFin1,100000)
plt.plot(alfa1(r1),beta1(r1),'b', label="a=0.1")
plt.plot(alfa1(r1),-beta1(r1),'b')
#purple, olivedrab


r2=np.linspace(rInic2,rFin2,100000)
plt.plot(alfa2(r2),beta2(r2),'royalblue',label="a=0.25")
plt.plot(alfa2(r2),-beta2(r2),'royalblue')
#gold, limegreen


r3=np.linspace(rInic3,rFin3,100000)
plt.plot(alfa3(r3),beta3(r3),'peru',label="a=0.5")
plt.plot(alfa3(r3),-beta3(r3),'peru')
#teal, darkolivegreen

r4=np.linspace(rInic4,rFin4,100000)

plt.plot(alfa4(r4),beta4(r4),'tomato',label="a=0.75")
plt.plot(alfa4(r4),-beta4(r4),'tomato')
#navy, lightseagreen

r5=np.linspace(rInic5,rFin5,100000)
plt.plot(alfa5(r5),beta5(r5),'r',label="a=0.9")
plt.plot(alfa5(r5),-beta5(r5),'r')


plt.axis('equal')
plt.title('Sombra de un agujero negro de Kerr')
plt.xlabel("α") 
plt.ylabel('β')

plt.legend()

plt.show()


# **Kerr-Newman**
# 
# Gráfica de $16Q(a^2-Q)+8QQ'r-Q'^2r^2$ utilizada para encontrar los valores límites de r.
# 
# ![picture](https://drive.google.com/uc?id=1pXJMIoCQvEoti18RvX0hUExsP4ZTIF3c)
# 
# Es importante resaltar que para Kerr-Newman se introduce un valor adicional: la carga eléctrica, $q$. Para el presente análisis, se toma $q=0.5$.
# 

# In[24]:


q=0.5


# El proceso a seguir es análogo al anterior:

# In[25]:


a11=0.15

def anul11(r):
  Q=r**2-2*M*r+a11**2+q**2
  Qp=2*r-2*M
  return 16*Q*(a11**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices11(A,B,nmax,tolerancia):
  fA=anul11(A)
  fB=anul11(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul11(A)
    if abs(d)<tolerancia:
      break
  return A

rInic11=HallarRaices11(2,2.6,1000,0.0000001)
rFin11=HallarRaices11(3.4,3.8,1000,0.0000001)

def alfa11(r):
  Q=r**2-2*M*r+a11**2+q**2
  Qp=2*r-2*M
  xi=((a11**2+r**2)*Qp-4*r*Q)/(a11*Qp)
  return -xi/np.sin(theta)

def beta11(r):
  Q=r**2-2*M*r+a11**2+q**2
  Qp=2*r-2*M
  xi=((a11**2+r**2)*Qp-4*r*Q)/(a11*Qp)
  eta=(r**2/(a11**2*Qp**2))*(anul11(r))
  return np.sqrt(eta+a11**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[26]:


a22=0.50

def anul22(r):
  Q=r**2-2*M*r+a22**2+q**2
  Qp=2*r-2*M
  return 16*Q*(a22**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices22(A,B,nmax,tolerancia):
  fA=anul22(A)
  fB=anul22(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul22(A)
    if abs(d)<tolerancia:
      break
  return A

rInic22=HallarRaices22(1.8,2.2,1000,0.0000001)
rFin22=HallarRaices22(3.4,4.0,1000,0.0000001)

def alfa22(r):
  Q=r**2-2*M*r+a22**2+q**2
  Qp=2*r-2*M
  xi=((a22**2+r**2)*Qp-4*r*Q)/(a22*Qp)
  return -xi/np.sin(theta)

def beta22(r):
  Q=r**2-2*M*r+a22**2+q**2
  Qp=2*r-2*M
  xi=((a22**2+r**2)*Qp-4*r*Q)/(a22*Qp)
  eta=(r**2/(a22**2*Qp**2))*(anul22(r))
  return np.sqrt(eta+a22**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[27]:


a33=0.86

def anul33(r):
  Q=r**2-2*M*r+a33**2+q**2
  Qp=2*r-2*M
  return 16*Q*(a33**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices33(A,B,nmax,tolerancia):
  fA=anul33(A)
  fB=anul33(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul33(A)
    if abs(d)<tolerancia:
      break
  return A

rInic33=HallarRaices33(1.0,1.2,1000,0.0000001)
rFin33=HallarRaices33(3.8,4.2,1000,0.0000001)

def alfa33(r):
  Q=r**2-2*M*r+a33**2+q**2
  Qp=2*r-2*M
  xi=((a33**2+r**2)*Qp-4*r*Q)/(a33*Qp)
  return -xi/np.sin(theta)

def beta33(r):
  Q=r**2-2*M*r+a33**2+q**2
  Qp=2*r-2*M
  xi=((a33**2+r**2)*Qp-4*r*Q)/(a33*Qp)
  eta=(r**2/(a33**2*Qp**2))*(anul33(r))
  return np.sqrt(eta+a33**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[28]:


r11=np.linspace(rInic11,rFin11,100000)
plt.plot(alfa11(r11),beta11(r11),'b', label="a=0.15")
plt.plot(alfa11(r11),-beta11(r11),'b')
#purple, olivedrab


r22=np.linspace(rInic22,rFin22,100000)
plt.plot(alfa22(r22),beta22(r22),'peru',label="a=0.5")
plt.plot(alfa22(r22),-beta22(r22),'peru')
#gold, limegreen


r33=np.linspace(rInic33,rFin33,100000)
plt.plot(alfa33(r33),beta33(r33),'r',label="a=0.86")
plt.plot(alfa33(r33),-beta33(r33),'r')


plt.axis('equal')
plt.title('Sombra de un agujero negro de Kerr-Newman ')
plt.xlabel("α") 
plt.ylabel('β')
plt.legend()

plt.show()


# *Bardeen-rotante*
# De manera análoga a las anteriores, se grafica para facilitar la obtención de las raíces.
# 
# ![picture](https://drive.google.com/uc?id=164kfqyMu34Nx2ry4UU6rp1YvCJOK9xAS)
# 
# 
# En Bardeen-rotante se añade una carga magnética a la configuración, dada por la cantidad $g$. En adelante, se considera $g=0.5$.

# 

# In[31]:


g=0.5


# Similarmente, se procede a configurar cada caso particular.

# In[32]:


a111=0.20

def anul111(r):
  Q=r**2+a111**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  return 16*Q*(a111**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices111(A,B,nmax,tolerancia):
  fA=anul111(A)
  fB=anul111(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul111(A)
    if abs(d)<tolerancia:
      break
  return A

rInic111=HallarRaices111(2.0,2.5,1000,0.0000001)
rFin111=HallarRaices111(3.2,3.8,1000,0.0000001)

def alfa111(r):
  Q=r**2+a111**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a111**2+r**2)*Qp-4*r*Q)/(a111*Qp)
  return -xi/np.sin(theta)

def beta111(r):
  Q=r**2+a111**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a111**2+r**2)*Qp-4*r*Q)/(a111*Qp)
  eta=(r**2/(a111**2*Qp**2))*(anul111(r))
  return np.sqrt(eta+a111**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[33]:


a222=0.40

def anul222(r):
  Q=r**2+a222**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  return 16*Q*(a222**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices222(A,B,nmax,tolerancia):
  fA=anul222(A)
  fB=anul222(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul222(A)
    if abs(d)<tolerancia:
      break
  return A

rInic222=HallarRaices222(1.8,2.2,1000,0.0000001)
rFin222=HallarRaices222(3.4,3.8,1000,0.0000001)

def alfa222(r):
  Q=r**2+a222**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a222**2+r**2)*Qp-4*r*Q)/(a222*Qp)
  return -xi/np.sin(theta)

def beta222(r):
  Q=r**2+a222**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a222**2+r**2)*Qp-4*r*Q)/(a222*Qp)
  eta=(r**2/(a222**2*Qp**2))*(anul222(r))
  return np.sqrt(eta+a222**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[34]:


a333=0.60

def anul333(r):
  Q=r**2+a333**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  return 16*Q*(a333**2-Q)+8*r*Q*Qp-r**2*Qp**2

def HallarRaices333(A,B,nmax,tolerancia):
  fA=anul333(A)
  fB=anul333(B)
  if abs(fA)>abs(fB):
    aux=B
    auxF=fB
    B=A
    A=aux
    fB=fA
    fA=auxF
  for n in range(2,nmax+1):
    if abs(fA)>abs(fB):
      aux=B
      auxF=fB
      B=A
      A=aux
      fB=fA
      fA=auxF
    d=(B-A)/(fB-fA)
    B=A
    fB=fA
    d=d*fA
    A=A-d
    fA=anul333(A)
    if abs(d)<tolerancia:
      break
  return A

rInic333=HallarRaices333(1.5,1.8,1000,0.0000001)
rFin333=HallarRaices333(3.5,4.0,1000,0.0000001)

def alfa333(r):
  Q=r**2+a333**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a333**2+r**2)*Qp-4*r*Q)/(a333*Qp)
  return -xi/np.sin(theta)

def beta333(r):
  Q=r**2+a333**2-2*M*r**4/(r**2+g**2)**(3/2)
  Qp=2*r-8*M*r**3*(r**2+g**2)**(-3/2)+6*M*r**5*(r**2+g**2)**(-5/2)
  xi=((a333**2+r**2)*Qp-4*r*Q)/(a333*Qp)
  eta=(r**2/(a333**2*Qp**2))*(anul333(r))
  return np.sqrt(eta+a333**2*(np.cos(theta))**2-xi**2/(np.tan(theta))**2)


# In[35]:


r111=np.linspace(rInic111,rFin111,100000)
plt.plot(alfa111(r111),beta111(r111),'b', label="a=0.2")
plt.plot(alfa111(r111),-beta111(r111),'b')
#purple, olivedrab


r222=np.linspace(rInic222,rFin222,100000)
plt.plot(alfa222(r222),beta222(r222),'peru',label="a=0.4")
plt.plot(alfa222(r222),-beta222(r222),'peru')
#gold, limegreen


r333=np.linspace(rInic333,rFin333,100000)
plt.plot(alfa333(r333),beta333(r333),'r',label="a=0.6")
plt.plot(alfa333(r333),-beta333(r333),'r')
#teal, darkolivegreen


plt.axis('equal')

plt.title('Sombra de un agujero negro Bardeen-rotante')
plt.xlabel("α") 
plt.ylabel('β')

plt.legend()

plt.show()


# **Comparación de la gráfica con la sombra del agujero negro en M87**
# 
# 
# Finalmente, a continuación se visualiza la sombra del agujero negro en M87* con una de las gráficas obtenidas para Kerr.
# <figure>
# <center>
# <img src='https://drive.google.com/uc?id=15jF21c7KBasmOg7sygiaoTqWraic_k-E'/>
# <figcaption>Gráfica de la sombra de un gujero negro de Kerr con a=0.9 sobrepuesta en la sombra del agujero negro M87*</figcaption></center>
# </figure>
# 
# 
# Como método de comparación en el achatamiento de la sombra se sobrepone también un círculo color negro. 
# <figure>
# <center>
# <img src='https://drive.google.com/uc?id=1AZUpTl69V8ZXQxV-pP-bf9ISuPjBarmG'/>
# <figcaption>Gráfica de la sombra de un gujero negro de Kerr con a=0.9 sobrepuesta en la sombra del agujero negro M87* con un círculo perfecto como comparación</figcaption></center>
# </figure>

# *Bibliografía*
# 
# 
# *   Wild, F. (10/07/2022). Black Holes. https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-a-black-hole-k4.html
# *    Contreras, E., Ramirez–Velasquez, J.M., Rincón, Á. et al. Black hole 
# 
# *   Shadow of a rotating polytropic black hole by the Newman–Janis algorithm without complexification. Eur. Phys. J. C 79, 802 (2019). https://doi.org/10.1140/epjc/s10052-019-7309-z
# *   Amarilla, L. (2013). Sombras de agujeros negros en teorías alternativas de gravitación (Doctoral dissertation, Universidad de Buenos Aires. Facultad de Ciencias Exactas y Naturales).
# 

# In[ ]:




