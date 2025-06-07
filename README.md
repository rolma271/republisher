# republisher

## Clonar el repositorio

```console
cd ~/ros2_ws/ 
git clone https://github.com/rolma271/republisher.git
```

## Construir el workspace

```console
cd ~/ros2_ws
colcon build --packages-select republisher --symlink-install
source install/setup.bash
```

## Cómo lanzar
Como lanzar el ejemplo:

```console
cd republisher
ros2 launch republisher republisher.launch.py
```