import streamlit as st
from PIL import Image
from main import wrap

wrap()
menu = st.sidebar.radio('Двумерная задача',
                        (
    "Расчетная область",
    "Постановка задачи", 
                        ))


if menu == "Расчетная область":
    """
## Расчетная область
Предполагается, что задача рассматривается в следующей области
    
"""
    st.image(Image.open('./oblast.png'), 'Расчетная область')
    r"""
$\Gamma_D$ - границы, на которых задается потенциал 
($\Gamma_D = \Gamma_1 \cup \Gamma_6$)

$\Gamma_R$ - граница на которой имеется теплообмен с окружающей средой
($\Gamma_R = \Gamma_1 \cup \Gamma_2 \cup \Gamma_3 \cup \Gamma_4$)

$\Omega_1$ - область с веществом, на котором создается разность потенциалов

$\Omega_2$ - область с веществом, проводящим ток, которое нагревается
"""

if menu == "Постановка задачи":
    r"""
## Математическая модель
 
 
**Уравнения  для температуры и электрического потенциала**

$\begin{aligned}
{-}\textrm{div} \left( \sigma \textrm{grad} \, \varphi \right) = 0
\end{aligned}$

$\begin{aligned}
C \frac{\partial u}{\partial t} - \textrm{div} \left( k \textrm{grad} \, u \right) = \sigma |\textrm{grad} \, \varphi |^2
\end{aligned}$

для $\bm x \in \Omega$,  $\Omega = \Omega_1 \cup \Omega_2$ и $t \in [0, T]$ 

$u$ - температура

$\varphi$ - электрический потенциал

$C$ - объемная теплоемкость проводящей среды

$k$ - коэффициент теплопроводности

$\sigma$ - коэффициент электропроводности

**Начальное условие**

$\begin{aligned}
u(\bm x, 0) = u_0, \quad \bm x \in \Omega
\end{aligned}$

**Граничные условия для температуры**

$\begin{aligned}
-k \frac{\partial u}{\partial n} (\bm x, t)  = \alpha \left( u - T_{air} \right), \quad \bm x \in  \Gamma_R
\end{aligned}$

$\begin{aligned}
-k \frac{\partial u}{\partial n} (\bm x, t)  = 0, \quad \bm x \in \partial \Omega / \Gamma_R
\end{aligned}$

**Граничные условия для потенциала**

$\begin{aligned}
\varphi(\bm x, t) = g, \quad \bm x \in \Gamma_D
\end{aligned}$


$\begin{aligned}
-\sigma \frac{\partial\varphi}{\partial n} (\bm x, t)  = 0, \quad \bm x \in  \partial \Omega / \Gamma_D.
\end{aligned}$

$\Gamma_D$ - границы, на которых задается потенциал 
($\Gamma_D = \Gamma_1 \cup \Gamma_6$)

$\Gamma_R$ - граница на которой имеется теплообмен с окружающей средой

$T_{air}$ - температура окружающей среды

$\alpha$ - коэффициент теплоотдачи 
($\Gamma_R = \Gamma_1 \cup \Gamma_2 \cup \Gamma_3 \cup \Gamma_4$)


    """