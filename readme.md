# Métodos Numéricos
## Trabajo Práctico: JACOBI
## UNSAM, 1er Cuatrimestre 2023

## Instalacion
- Accede al directorio del proyecto.

```bash
cd LU
```

- Crear un entorno virtual. (opcional)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Instala las dependencias.

```bash
pip3 install -r requirements.txt
```

- Ejecuta el programa.

```bash
python3 lu.py
```

- Sigue las instrucciones que aparecen en consola.

## Integrantes del equipo
- Agustin Narvaez
- Tomas Venturini

## Ejemplos capturados
### Matriz de 3x3
[4.24748  | 0.575032 | 0.162125]
[0.575032 │ 4.9733   │ 1.10846 ]
[0.162125 │ 1.10846  │ 4.22216 ]
Vector b: [3, 4, 5]
 - (5 iteraciones)
   - Matriz de iteracion H:
[0.706301 │ 0.804295 │ 1.18423 ]
[0.552213 │ 0.458686 │ 0.945951]
[0.608097 │ 0.52961  │ 1.0426  ]
[0.594806 │ 0.501606 │ 1.02184 ]
[0.59939  │ 0.507772 │ 1.0297  ]
    - Norma de la matriz de iteración H: 1.295136395153109
    - Solución aproximada con Jacobi: [0.59938981 0.50777155 1.0296981 ]
    - Solución exacta del sistema: [0.59856118 0.50586642 1.02843552]
    - Norma de la diferencia entre las soluciones: 0.0024311002761044586

 - (20 iteraciones)
- Matriz de iteracion H:
[0.706301 │ 0.804295 │ 1.18423 ]
[0.592894 │ 0.458686 │ 0.945952]
[0.640593 │ 0.524906 │ 1.04104 ]
[0.631265 │ 0.498198 │ 1.02182 ]
[0.634954 │ 0.503559 │ 1.02919 ]
[0.6342   │ 0.50149  │ 1.02765 ]
[0.634486 │ 0.501922 │ 1.02822 ]
[0.634425 │ 0.501762 │ 1.02809 ]
[0.634447 │ 0.501797 │ 1.02814 ]
[0.634443 │ 0.501784 │ 1.02813 ]
[0.634444 │ 0.501787 │ 1.02813 ]
[0.634444 │ 0.501786 │ 1.02813 ]
....
....
....
[0.634444 │ 0.501786 │ 1.02813 ]
    - Norma de la matriz de iteración H: 1.308189820765761
    - Solución aproximada con Jacobi: [0.63444404 0.50178614 1.02813036]
    - Solución exacta del sistema: [0.63444404 0.50178614 1.02813036]
    - Norma de la diferencia entre las soluciones: 1.134260957342208e-11


### Matriz de 4x4
[4.79884  │ 1.81028 │ 1.01547  │ 0.750035]
[1.81028  │ 5.25631 │ 1.05758  │ 1.08069 ]
[1.01547  │ 1.05758 │ 4.54271  │ 0.862923]
[0.750035 │ 1.08069 │ 0.862923 │ 4.6422  ]

Vector b: [3, 4, 5, 6]

 - (2 iteraciones)
   - Matriz de iteracion H:
[0.62515    │ 0.76099   │ 1.10066  │ 1.29249]
[-0.0968376 │ 0.0584979 │ 0.538236 │ 0.80973]
    - Norma de la matriz de iteración H: 0.9788568999675532
    - Solución aproximada con Jacobi: [-0.09683756  0.05849791  0.53823629  0.80973021]
    - Solución exacta del sistema: [0.17142002 0.3292725  0.78780971 1.04169722]
    - Norma de la diferencia entre las soluciones: 0.5112500339756902

 - (5 iteraciones)
- Matriz de iteracion H:
[0.625151   │ 0.76099   │ 1.10066  │ 1.29249 ]
[-0.096838  │ 0.0584971 │ 0.538236 │ 0.809731]
[0.362632   │ 0.519568  │ 0.954878 │ 1.19447 ]
[0.0404044  │ 0.198395  │ 0.671744 │ 0.935448]
[0.261958   │ 0.419592  │ 0.867749 │ 1.11491]
    - Norma de la matriz de iteración H: 1.496893171750088
    - Solución aproximada con Jacobi: [0.26195818 0.4195918  0.86774922 1.11490856]
    - Solución exacta del sistema: [0.17142019 0.32927234 0.78780977 1.04169755]
    - Norma de la diferencia entre las soluciones: 0.16764515994603946

### Conclusión
En ambos ejemplos de matrices de 3x3 y 4x4, se puede ver que a medida que aumentan las iteraciones, la norma de la matriz de iteración H aumenta, por lo que la convergencia es más lenta. Además, se puede ver que la norma de la diferencia entre las soluciones disminuye a medida que aumentan las iteraciones, por lo que la solución aproximada se acerca más a la solución exacta del sistema.