import os
import sys

# PyInstaller가 libmlx.dylib를 _MEIPASS 최상위에 복사하는데,
# MLX C++가 dladdr로 자기 경로 기준 같은 디렉토리에서 mlx.metallib를 찾는다.
# 실제 metallib은 mlx/lib/ 하위에 있으므로 symlink로 연결한다.
meipass = getattr(sys, '_MEIPASS', None)
if meipass:
    metallib_src = os.path.join(meipass, 'mlx', 'lib', 'mlx.metallib')
    metallib_dst = os.path.join(meipass, 'mlx.metallib')
    if os.path.exists(metallib_src) and not os.path.exists(metallib_dst):
        os.symlink(metallib_src, metallib_dst)
