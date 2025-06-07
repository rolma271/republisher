# republisher

## Clonar el repositorio

```console
cd ~/ros2_ws/ 
git clone https://github.com/rolma271/republisher.git
```

## Construir el workspace

```console
colcon build --packages-select republisher republisher_interfaces
source install/setup.bash
```

## Cómo lanzar
Como lanzar el ejemplo:

```console
cd republisher
ros2 launch republisher republisher.launch.py
```