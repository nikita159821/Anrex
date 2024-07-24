import os
import xml.etree.ElementTree as ET

# Получаем текущий рабочий каталог
workspace = os.environ.get('GITHUB_WORKSPACE')

# Определяем пути к файлам
report_path = os.path.join(workspace, 'tests_main_page', 'report.xml')
modified_report_path = os.path.join(workspace, 'tests_main_page', 'modified_report.xml')

# Загрузите и проанализируйте XML файл
if os.path.exists(modified_report_path):
    tree = ET.parse(modified_report_path)
else:
    tree = ET.parse(report_path)
root = tree.getroot()

# Создайте новый корневой элемент, который будет заменять <testsuites>
new_root = ET.Element('root')

# Добавьте в новый корневой элемент все элементы <testsuite>
for testsuite in root:
    new_root.append(testsuite)

# Создайте новое дерево с новым корневым элементом
new_tree = ET.ElementTree(new_root)

# Сохраните изменения в новый файл
new_tree.write(modified_report_path, encoding='utf-8', xml_declaration=True)
print(f"Modified report saved at: {modified_report_path}")
