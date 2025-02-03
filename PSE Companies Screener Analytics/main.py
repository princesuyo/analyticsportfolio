import requests
from bs4 import BeautifulSoup
import pandas as pd
import os 
import time
import shutil

file_directory = 'data'

annual_directory = 'annual'
company_directory = 'company'
qtr_directory = 'quarterly'

annual_file = 'annual.csv'
qtr_file = 'quarter.csv'
company_file = 'companies.csv'

directories = [annual_directory, company_directory, qtr_directory]

def make_directories():
	for d in directories:
		if not os.path.exists(os.path.join(file_directory, d)):
			os.makedirs(os.path.join(file_directory, d))

# GET ANNUAL TABLE
def get_annual_table(url):
	response = requests.get(url)

	# If response 200
	if response.status_code == 200:

		global year
		global df_annual
		global currency

		soup = BeautifulSoup(response.text, 'html.parser')

		# Extract first two tables for annual
		try:
			tables = soup.find_all('table')
			tables = tables[:2]

			dataframes = []

			for table in tables:
				headers = []
				rows = []

				header_row = table.find('tr')

				if header_row:
					headers = [th.text.strip() for th in header_row.find_all('th')]

				for row in table.find_all('tr')[1:]:
					cells = []
					th_cells = row.find_all('th')
					td_cells = row.find_all('td')

					if th_cells:
						cells.extend([th.text.strip() for th in th_cells])

					if td_cells:	
						cells.extend([td.text.strip() for td in td_cells])

					if len(cells) == len(headers):
						rows.append(cells)
					else:
						print(cells, ': skipped due to column mismatch')

				df = pd.DataFrame(rows, columns = headers if headers else None)
				dataframes.append(df)


			df_annual = pd.concat(dataframes, axis = 0)

			year = soup.find_all('p', class_ = 'textCont')
			year = [y.text.strip() for y in year][1].split('\n')[0].split(':')[1].strip()
			currency = soup.find_all('p', class_ = 'textCont')
			currency = [c.text.strip() for c in currency][1].split('\n')[1].split(':')[1].strip()

		except Exception as e:
			print('Annual: ', e)

	# If response != 200
	else:
		print(response.status_code)

def get_qtr_table(url):
	response = requests.get(url)

	# If response 200
	if response.status_code == 200:

		global df_qtr
		global date_qtr

		soup = BeautifulSoup(response.text, 'html.parser')
		# Extract Quarterly Income table
		try:
			table = soup.find_all('table')
			table = table[-1]

			# for table in tables:
			rows = []
			headers = []

			header_row = table.find('tr')

			if header_row:
				headers = [th.text.strip() for th in header_row.find_all('th')]

			for row in table.find_all('tr')[1:]:
				cells = []
				th_cells = row.find_all('th')
				td_cells = row.find_all('td')

				if th_cells:
					cells.extend([th.text.strip() for th in th_cells])

				if td_cells:	
					cells.extend([td.text.strip() for td in td_cells])

				if len(cells) == len(headers):
					rows.append(cells)
				else:
					print(cells, ': skipped due to column mismatch')

			df_qtr = pd.DataFrame(rows, columns = headers if headers else None)

			# df_qtr = df
			qtr_header = soup.find('h3', string = 'Quarterly')
			date_qtr = qtr_header.find_next('p', class_ = 'textCont').text.strip()
			date_qtr = date_qtr.split('\n')[0].split(':')[1].strip()

		except Exception as e:
			print('Quarterly', e)

	# If response != 200
	else:
		print(response.status_code)

def get_stock_info(url):
	response = requests.get(url)
	global df_stock

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')

		try: 
			outstanding_shares = soup.find('th', string = 'Outstanding Shares').find_next_sibling('td').text.strip()
			average_price = soup.find('th', string='Average Price').find_next_sibling('td').text.strip()
			volume = soup.find('th', string='Volume').find_next_sibling('td').text.strip()

			df_stock = pd.DataFrame({
				'Item' : ['Outstanding Shares', 'Average Price', 'Volume'],
				'Current Year' : [outstanding_shares, average_price, volume]
			})

		except Exception as e:
			new_rows = pd.DataFrame({
				'Item' : ['Outstanding Shares', 'Average Price', 'Volume'],
				'Current Year' : ['0', '0', '0']
			})
			
	else:
		print(response.status_code)

def get_company_info(url):
	global sector
	global subsector
	global incorp_date
	global company
	global df_company

	response = requests.get(url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		try:
			sector = soup.find('th', string = 'Sector').find_next_sibling('td').text.strip()
			subsector = soup.find('th', string = 'Subsector').find_next_sibling('td').text.strip()
			incorp_date = soup.find('th', string = 'Incorporation Date').find_next_sibling('td').text.strip()
			company = soup.find('div', class_ = 'compInfo').find('p').text.strip()

			df_company = pd.DataFrame({
				'Company': [company],
				'Sector': [sector],
				'Subsector': [subsector],
				'Incorporation Date': [incorp_date]
				})

		except Exception as e:
			print(e)
	else:
		print(response.status_code)

def remove_duplicates(file):

	df = pd.read_csv(file)

	try: 
		df = df.drop_duplicates(subset = ['Item', 'Company', 'Date'])
	except: 
		df = df.drop_duplicates()

	df.to_csv(file, index = False)

def main():

	make_directories()

	for i in range(1,710):
		url_financial = f'https://edge.pse.com.ph/companyPage/financial_reports_view.do?cmpy_id={i}'
		url_stock = f'https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={i}'
		url_company = f'https://edge.pse.com.ph/companyInformation/form.do?cmpy_id={i}'

		get_annual_table(url = url_financial) # GLOBALS: company, year, currency, df_annual, df_qtr, date_qtr
		get_qtr_table(url = url_financial)
		get_stock_info(url = url_stock) # GLOBALS: df_stock
		get_company_info(url = url_company) # GLOBALS: sector, subsector

		# print(company, sector, subsector, incorp_date)

		try:
			df_annual1 = pd.concat([df_annual, df_stock], ignore_index = True)
			df_annual1['Company'] = company 
			df_annual1['Date'] = year 

			df_qtr['Company'] = company
			df_qtr['Date'] = date_qtr

			annual_file_exists = os.path.isfile(os.path.join(file_directory, annual_directory, annual_file))
			df_annual1.to_csv(f'{file_directory}/{annual_directory}/{annual_file}', index = False, mode = 'a', header = not annual_file_exists)

			qtr_file_exists = os.path.isfile(os.path.join(file_directory, qtr_directory, qtr_file))
			df_qtr.to_csv(f'{file_directory}/{qtr_directory}/{qtr_file}', index = False, mode = 'a', header = not qtr_file_exists)

			company_file_exists = os.path.isfile(os.path.join(file_directory, company_directory, company_file))
			df_company.to_csv(f'{file_directory}/{company_directory}/{company_file}', index = False, mode = 'a', header = not company_file_exists)

			print(i, company, 'scraped')

		except Exception as e:
			print(i, e)

		time.sleep(2)

	files = [
				f'{file_directory}/{annual_directory}/{annual_file}',
				f'{file_directory}/{qtr_directory}/{qtr_file}',
				f'{file_directory}/{company_directory}/{company_file}'
			]

	for file in files:
		remove_duplicates(file)

if __name__ == '__main__':
	main()

