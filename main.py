from text_mining import *

if __name__ == '__main__':
    start_time = time.time()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Data Collecting
    collect_html_from(
        add_prefix(name_list=get_list_from('./name_list.txt'),
                   prefix='https://scholar.google.com/scholar?hl=en&as_vis=0&as_sdt=0%2C5&q=',
                   prefix2=8026))

    sendMail(title_text=f'[수집완료] 경과시간 {time.time() - now} ', body_text='수집완료 Done', to_ad='team.k0konutz@gmail.com')

    col_list = ['No', 'Name', 'scholar URL', 'Reference(Oldest)', 'Reference(Newest)', 'Cited Total Num',
                'Search Count Num']
    output_file_name = 'Output_Crawling Project_scholar.google.com_8026ea_220622_v1.0.xlsx'
    make_output_file(output_file_name=output_file_name, col_list=col_list)

    sendMail(title_text=f'[처리완료] 경과시간 {time.time() - now} ', body_text='Done', to_ad='team.k0konutz@gmail.com')
