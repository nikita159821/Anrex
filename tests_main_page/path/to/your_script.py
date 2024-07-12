import xml.etree.ElementTree as ET
import os

# Получаем текущий рабочий каталог
workspace = os.environ.get('GITHUB_WORKSPACE')

# Загрузите и проанализируйте XML файл
tree = ET.parse(os.path.join(workspace, 'junit-report.xml'))
root = tree.getroot()

# Создайте новый корневой элемент, который будет заменять <testsuites>
new_root = ET.Element('root')  # Можно использовать другое имя, если нужно

# Добавьте в новый корневой элемент все элементы <testsuite>
for testsuite in root:
    new_root.append(testsuite)

# Создайте новое дерево с новым корневым элементом
new_tree = ET.ElementTree(new_root)

# Сохраните изменения в новый файл
new_tree.write(os.path.join(workspace, 'modified_report.xml'), encoding='utf-8', xml_declaration=True)