import text_mining
from text_mining import *

if __name__ == '__main__':
    start_time = time.time()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Data Collecting
    text_mining.collect_html_from(
        add_prefix(name_list=get_list_from('./name_list.txt'),
                   prefix='https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=',
                   prefix2=8026))

    sendMail(
        article='Done',
        new_num=80, to_ad='team.k0konutz@gmail.com')
    time.sleep(100)
    os.system('shutdown -s -f')

    # """
    # Data conversion
    # """
    # fi = open('output_data','w',encoding='utf-8')
    # for i in range(2,load_input_data_sheet.max_row+1):
    #     i_no = load_input_data_sheet.cell(row=i,column=1).value
    #     i_name = load_input_data_sheet.cell(row=i, column=2).value
    #     i_url = re.sub(r'\+\(.*\)', '', i_name.strip().replace('  ', '+').replace(' ','+').replace('\n',''))
    #     i_us_count = load_input_data_sheet.cell(row=i, column=9).value
    #     if 'United States' in i_us_count:
    #         i_us = 1
    #     else:
    #         i_us = 0
    #     i_count = str(i_us_count).count(';')
    #     fi.writelines(str(i_no)+'|'+i_name+'|https://scholar.google.com/scholar?hl=en&q='+i_url+'|'+str(i_us)+'|'+str(i_count)+'\n')
    # fi.close()
    #
    # """
    # Data Collecting
    # """
    # all_data = []
    # fs = open('output_data', 'r')
    # out_list = []
    # for i in fs.readlines():
    #     out_list.append(i.split('|')[2])
    # fs.close()
    # mc.collecting_start(out_list)
    #
    # """
    # Data Processing
    # """
    # excel_file_name = 'Output_Crawling Project_scholar.google.com_615ea_220612_v2.0.xlsx'
    # col_list = ['No',	'Name',	'URL',	'Reference(Oldest)',	'Reference(Newest)','Cited Total Num', 'Search Count Num','US','Countries']
    #
    # wb = Workbook()
    # ws = wb.active
    # ws.append(col_list)
    #
    # fs = open('output_data', 'r')
    # for line_comp in fs.readlines():
    #
    #     comp_no = line_comp.split('|')[0]
    #     comp_name = line_comp.split('|')[1]
    #     comp_url = line_comp.split('|')[2]
    #     comp_us = line_comp.split('|')[3]
    #     comp_countries_num = line_comp.split('|')[4]
    #
    #     f = open('./datas/' + comp_no+'.html', 'r', encoding='utf-8')
    #     comp_file_text = f.read()
    #     f.close()
    #
    #     if "robot" in comp_file_text:
    #         print('!!(F)Robot!!! : '+comp_url)
    #         continue
    #
    #     comp_date_list = tm.template_scholar_google_com(comp_file_text)
    #     ws.append([int(comp_no),comp_name,comp_url,int(comp_date_list[2]),int(comp_date_list[3]),int(comp_date_list[1]),int(comp_date_list[0]),int(comp_us),int(comp_countries_num)])
    #     wb.save(excel_file_name)
    #     print('['+str(comp_no)+'/'+str(len(out_list))+'] : ' + comp_name +' '+ comp_url)
    #
    # wb.close()
    # fs.close()
    #
    # print('Completed [' + str(now) + ' > ' + str(round(time.time() - start_time, 2)) + ']')
