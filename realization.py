import streamlit as st
from PIL import Image
from main import wrap

wrap()


menu = st.sidebar.radio(
    "Численная реализация",
    (
        "Конечно-элементная аппроксимация",
        "Построение сетки",
    ),
)

if menu == "Конечно-элементная аппроксимация":
    r"""
    ## Конечно-элементная аппроксимация

    Проведем аппроксимацию по пространству задачи с использованием метода конечных элементов. Умножим уравнение для температуры на тестовую функцию v и проинтегрируем с использованием формулы Грина:

    $\begin{aligned}
    \int_{\Omega} (\sigma \nabla \varphi, \nabla v) \, dx = 0, \quad \forall v \in \hat{V}.
    \end{aligned}$

    Аналогично, уравнение для температуры умножим на тестовую функцию \( q \) и проинтегрируем:
    $\begin{aligned}
    \int_{\Omega} C \frac{\partial u}{\partial t} q \, dx + \int_{\Omega} (k \nabla u, \nabla q) \, dx + \int_{\Omega} \alpha (u - T_{\text{air}}) q \, dx = \int_{\Omega} \sigma |\nabla \varphi|^2 q \, dx, \quad \forall q \in \hat{Q}.
    \end{aligned}$

    Здесь

    """

    st.latex(r'''\ v \in \hat{V} = \{ v \in H^1(\Omega) : v|_{\Gamma_D} = 0\}, q \in \hat{V} =  H^1(\Omega) ''')
    st.latex(r'''\ \varphi \in Q = \{ v \in H^1(\Omega) : v|_{\Gamma_D} = g\}, u \in Q =  H^1(\Omega) ''')
    r'''где $\ H^1(\Omega)$  пространство  Соболева, состоящее из функций $v$ таких, что $v^2$ и $|\nabla|^2$ имеют конечный интеграл в $\Omega$'''

    r'''Для аппроксимации по времени уравнения для температуры, применим стандартную чисто неявную схему'''

    r'''$\begin{aligned}
\int_{\Omega} (\sigma(u^n) \nabla \varphi^{n+1}, \nabla v) \, dx = 0,
\end{aligned}$'''

    r'''$\begin{aligned}
    \int_{\Omega} C\frac{u^{n+1} - u^n}{\tau} q \, dx + \int_{\Omega} (k \nabla u^{n+1}, \nabla q) \, dx + \int_{\Omega} \alpha (u^{n+1} - T_{\text{air}}) q \, dx = \int_{\Omega} \sigma(u^n) |\nabla \varphi^{n+1}|^2 q \, dx.
    \end{aligned}$'''

    r'''
    Для численного решения мы должны перейти от непрерывной вариационной задачи к дискретной задаче. Введем конечномерные пространства $ V_h \subset V$, $ Q_h \subset Q $ и $ \hat{V}_h \subset \hat{V} $, $ \hat{Q}_h \subset \hat{Q}$  и определим в них дискретную задачу: найти $ u_h \in Q_h $, $ \varphi_h \in V_h $ такие что
    '''

    r'''
    $\begin{aligned}
\int_{\Omega} (\sigma(u_h^n) \nabla \varphi_h^{n+1}, \nabla v_h) \, dx = 0, \quad \forall v_h \in \hat{V}_h,
\end{aligned}$'''

    r'''
    $\begin{aligned}
\int_{\Omega} C\frac{u_h^{n+1} - u_h^n}{\tau} q_h \, dx + \int_{\Omega} (k \nabla u_h^{n+1}, \nabla q_h) \, dx + 
\int_{\Omega} \alpha (u_h^{n+1} - T_{\text{air}}) q_h \, dx = \int_{\Omega} \sigma(u_h^n) |\nabla \varphi_h^{n+1}|^2 q_h \, dx, \quad \forall q_h \in \hat{Q}_h.
\end{aligned}$    
'''

    r'''
    В качестве пространств $ V_h $ и $ Q_h $ будем использовать стандартные пространства лагранжевых конечных элементов.
    '''
if menu == "Построение сетки":
    """
    ## Построение сетки
    Для данной расчетной области был получена сетка (может быть получен ряд сеток разных размеров)
    """
    st.image(Image.open('./mesh1.png'), 'Сетка')

    expander = st.expander(" Код генератора сеток (Python) ")
    expander.code("""import gmsh 

gmsh.initialize()

gmsh.model.add("setk")

lc = 0.008
scale = 0.01

gmsh.model.geo.addPoint(0 * scale,5 * scale, 0, lc, 1)
gmsh.model.geo.addPoint(1* scale, 5 * scale,0, lc, 2)
gmsh.model.geo.addPoint(1* scale, 4.* scale, 0, lc/10, 3)
gmsh.model.geo.addPoint(4.7 * scale, 4. * scale, 0, lc, 4)
gmsh.model.geo.addPoint(5.0 * scale, 4. * scale, 0, lc, 5)
gmsh.model.geo.addPoint(5.0* scale, 0, 0, lc, 6)
gmsh.model.geo.addPoint(2.5* scale, 0, 0, lc, 7)
gmsh.model.geo.addPoint(0, 0, 0, lc, 8)
gmsh.model.geo.addPoint(4.7* scale, 0.3* scale, 0, lc/1, 9)
gmsh.model.geo.addPoint(0, 0.3* scale, 0, lc, 10)
gmsh.model.geo.addPoint(0, 3* scale, 0, lc/10, 11)
gmsh.model.geo.addPoint(1* scale, 3* scale, 0, lc/10, 12)

gmsh.model.geo.addLine(1,2,1)
gmsh.model.geo.addLine(2,3,2)
gmsh.model.geo.addLine(3,4,3)
gmsh.model.geo.addLine(4,5,4)
gmsh.model.geo.addLine(5,6,5)
gmsh.model.geo.addLine(6,7,6)
gmsh.model.geo.addLine(7,8,7)
gmsh.model.geo.addLine(8,10,8)
gmsh.model.geo.addLine(10,11,9)
gmsh.model.geo.addLine(11,1,10)
gmsh.model.geo.addLine(11,12,11)
gmsh.model.geo.addLine(12,3,12)
gmsh.model.geo.addLine(4, 9, 13)
gmsh.model.geo.addLine(9, 10, 14)

gmsh.model.geo.addCurveLoop([1,2,-12,-11,10],1)
gmsh.model.geo.addCurveLoop([11,12,3,13,14,9],2)
gmsh.model.geo.addCurveLoop([4, 5, 6, 7, 8, -14, -13],3)

gmsh.model.geo.addPlaneSurface([1],1)
gmsh.model.geo.addPlaneSurface([2],2)
gmsh.model.geo.addPlaneSurface([3],3)

gmsh.model.geo.synchronize()

gmsh.model.addPhysicalGroup(1,[1],1)
gmsh.model.addPhysicalGroup(1,[2],2)
gmsh.model.addPhysicalGroup(1,[3],3)
gmsh.model.addPhysicalGroup(1,[4,5],4)
gmsh.model.addPhysicalGroup(1,[6],5)
gmsh.model.addPhysicalGroup(1,[7],6)
gmsh.model.addPhysicalGroup(1,[8,9,10],7)

gmsh.model.addPhysicalGroup(2,[1,3],1)
gmsh.model.addPhysicalGroup(2,[2],2)

gmsh.model.mesh.generate(2)

gmsh.option.setNumber("Mesh.MshFileVersion", 2)
gmsh.write("./meshes/2Dmesh_NaN.msh")

gmsh.fltk.run()

gmsh.finalize()""")