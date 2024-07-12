import xml.etree.ElementTree as ET
import os

# Получаем текущий рабочий каталог
workspace = os.environ.get('GITHUB_WORKSPACE')

# Загрузите и проанализируйте XML файл
report_path = os.path.join(workspace, 'tests_basket_page', 'report.xml')
if os.path.exists(report_path):
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
    modified_report_path = os.path.join(workspace, 'tests_basket_page', 'modified_report.xml')
    new_tree.write(modified_report_path, encoding='utf-8', xml_declaration=True)
    print(f"Modified report saved at: {modified_report_path}")
else:
    print(f"File {report_path} does not exist.")
