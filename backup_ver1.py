#!/usr/bin/env python3

import os
import time

source = ['.', '../ch01']
target_dir = '..'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

