import subprocess
import openpyxl
import json

# 运行 GitHub CLI 命令并捕获输出（以JSON格式输出）
github_cli_command = "gh pr list --label 'contributor' --state merged --json number,title,url,author --limit 10000"
try:
    result = subprocess.run(github_cli_command, shell=True, capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    print("命令执行失败:", e)

# 解析 GitHub CLI 命令的JSON输出
json_output = result.stdout.strip()
prs_data = json.loads(json_output)

# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook()
sheet = workbook.active

# 设置表头
sheet['A1'] = 'PR Number'
sheet['B1'] = 'PR Title'
sheet['C1'] = 'PR URL'
sheet['D1'] = 'Author'

# 将 GitHub PR 数据写入 Excel 表格
for row_index, pr in enumerate(prs_data, start=2):
    pr_number = pr['number']
    pr_title = pr['title']
    pr_url = pr['url']
    author = pr['author']['login']  # 提取作者的登录名

    sheet[f'A{row_index}'] = pr_number
    sheet[f'B{row_index}'] = pr_title
    sheet[f'C{row_index}'] = pr_url
    sheet[f'D{row_index}'] = author

# 保存 Excel 文件
workbook.save('github_prs_with_author_1.1_merged.xlsx')

print("GitHub PR 列表（包含作者登录名）已保存到 github_prs_with_author_1.1.xlsx 文件中。")
