import xml.etree.ElementTree as ET
import os

# Получаем текущий рабочий каталог
workspace = os.getcwd()

# Путь к файлу с результатами теста
junit_report_path = os.path.join(workspace, 'path/to/report.xml')

# Загрузите и проанализируйте XML файл
tree = ET.parse(junit_report_path)
root = tree.getroot()

# Создайте новый корневой элемент, который будет заменять <testsuites>
new_root = ET.Element('root')  # Можно использовать другое имя, если нужно

# Добавьте в новый корневой элемент все элементы <testsuite>
for testsuite in root:
    new_root.append(testsuite)

# Создайте новое дерево с новым корневым элементом
new_tree = ET.ElementTree(new_root)

# Сохраните изменения в новый файл
modified_report_path = os.path.join(workspace, 'modified_report.xml')
new_tree.write(modified_report_path, encoding='utf-8', xml_declaration=True)
