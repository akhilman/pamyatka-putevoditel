all: ebook printbook txt upload

upload: putevoditel.txt putevoditel.ebook.pdf putevoditel.print.zip
	echo "cd /ildar/putevoditel/\nmput putevoditel.ebook.pdf putevoditel.print.zip putevoditel.txt" | cadaver webdav.h01.akhil.ru


###
## txt 
######

txt: putevoditel.txt

putevoditel.txt: ../putevoditel.txt
	cp ../putevoditel.txt putevoditel.txt
	unix2dos putevoditel.txt

###
## pdf для чтения с экрана
######
ebook: putevoditel.ebook.pdf

putevoditel.ebook.pdf: ../putevoditel.pdf
	cat ../putevoditel.pdf \
	    | python crop.py \
	    > putevoditel.ebook.pdf

###
## pdf для печати
######

printbook: putevoditel.print.zip 

putevoditel.print.zip: \
    putevoditel.print.pdf putevoditel-cover.print.pdf \
    putevoditel.print-booklet_odd.pdf putevoditel.print-booklet_even.pdf \
    putevoditel.print-cover-color.pdf \
    putevoditel.print-cover-grayscale.pdf \
    putevoditel.print-cover-for_yellow_papper.pdf \
    putevoditel.print-cover-interlayer.pdf \
    README.pdf \
    print-booklet_odd.shifted_for_my_printer.ps 
	zip tmp.putevoditel.print.zip putevoditel*.print*.pdf README.pdf
	mv tmp.putevoditel.print.zip putevoditel.print.zip


# обложка
putevoditel.print-cover-color.pdf: tmp.print-cover-color.ps
	ps2pdf13 tmp.print-cover-color.ps putevoditel.print-cover-color.pdf

tmp.print-cover-color.ps: tmp.print-cover.ps
	psselect -p1 tmp.print-cover.ps tmp.print-cover-color.ps

putevoditel.print-cover-grayscale.pdf: tmp.print-cover-grayscale.ps
	ps2pdf13 tmp.print-cover-grayscale.ps putevoditel.print-cover-grayscale.pdf

tmp.print-cover-grayscale.ps: tmp.print-cover.ps
	psselect -p2 tmp.print-cover.ps tmp.print-cover-grayscale.ps

putevoditel.print-cover-for_yellow_papper.pdf: tmp.print-cover-for_yellow_papper.ps
	ps2pdf13 tmp.print-cover-for_yellow_papper.ps putevoditel.print-cover-for_yellow_papper.pdf

tmp.print-cover-for_yellow_papper.ps: tmp.print-cover.ps
	psselect -p3 tmp.print-cover.ps tmp.print-cover-for_yellow_papper.ps

putevoditel.print-cover-interlayer.pdf: tmp.print-cover-interlayer.ps
	ps2pdf13 tmp.print-cover-interlayer.ps putevoditel.print-cover-interlayer.pdf

tmp.print-cover-interlayer.ps: tmp.print-cover.ps
	psselect -p4 tmp.print-cover.ps tmp.print-cover-interlayer.ps

tmp.print-cover.ps: ../print-cover.pdf
	gs \
	    -sDEVICE=pswrite -dNOCACHE \
	    -sOutputFile=tmp.print-cover.ps -q -dbatch -dNOPAUSE \
	    -dAutoRotatePages=/None \
	    -dQUIET "../print-cover.pdf" -c quit 

# плоский (векторезированный) pdf как есть
putevoditel.print.pdf: tmp.print-vectorized.ps
	ps2pdf13 tmp.print-vectorized.ps putevoditel.print.pdf

# нечетные страници с учетом звдига принтера моего
print-booklet_odd.shifted_for_my_printer.ps: tmp.print-booklet.ps
	pstops -pa4 "2:0(0,5.5)" tmp.print-booklet.ps print-booklet_odd.shifted_for_my_printer.ps      
	
# плоский (векторезированный) pdf раскиданный для печати и склейки
putevoditel.print-booklet_odd.pdf: tmp.print-booklet_odd.ps
	ps2pdf13 tmp.print-booklet_odd.ps putevoditel.print-booklet_odd.pdf

putevoditel.print-booklet_even.pdf: tmp.print-booklet_even.ps
	ps2pdf13 tmp.print-booklet_even.ps putevoditel.print-booklet_even.pdf

###

tmp.print-booklet_odd.ps: tmp.print-booklet.ps
	pstops -pa4 "2:0" tmp.print-booklet.ps tmp.print-booklet_odd.ps

tmp.print-booklet_even.ps: tmp.print-booklet.ps
	pstops -pa4 "2:1" tmp.print-booklet.ps tmp.print-booklet_even.ps

###

tmp.print-booklet.ps: tmp.print-vectorizedplusempty.ps 
	pstops -pa4 \
	    "4:1R(0,1h)+2R(0,0.5h),3R(0,1h)+0R(0,0.5h)"\
	    tmp.print-vectorizedplusempty.ps \
	    tmp.print-booklet.ps

tmp.print-vectorizedplusempty.ps: tmp.print-vectorized.ps tmp.print-emptystart.ps tmp.print-emptyend.ps
	psmerge -otmp.print-vectorizedplusempty.ps \
	    tmp.print-emptystart.ps \
	    tmp.print-vectorized.ps \
	    tmp.print-emptyend.ps

tmp.print-vectorized.ps: ../putevoditel.pdf
	gs \
	    -sDEVICE=pswrite -dNOCACHE \
	    -sOutputFile=tmp.print-vectorized.ps -q -dbatch -dNOPAUSE \
	    -dAutoRotatePages=/None \
	    -dQUIET "../putevoditel.pdf" -c quit 

tmp.print-emptystart.ps: tmp.print-empty.ps
	pstops -pa5 "4:0,1" tmp.print-empty.ps tmp.print-emptystart.ps

tmp.print-emptyend.ps: tmp.print-empty.ps
	pstops -pa5 "4:2,3" tmp.print-empty.ps tmp.print-emptyend.ps

tmp.print-empty.ps: ../empty.pdf
	gs \
	    -sDEVICE=pswrite -dNOCACHE \
	    -sOutputFile=tmp.print-empty.ps -q -dbatch -dNOPAUSE \
	    -dAutoRotatePages=/None \
	    -dQUIET "../empty.pdf" -c quit 

putevoditel-cover.print.pdf: ../cover.pdf
	gs \
	    -sDEVICE=pdfwrite -dNOCACHE \
	    -sOutputFile=putevoditel-cover.print.pdf -q -dbatch -dNOPAUSE \
	    -dQUIET "../cover.pdf" -c quit 

###
## Исходники получаемые из скрибуса
######

../empty.pdf:

../putevoditel.pdf:

../print-cover.pdf:

../putevoditel.txt:

## просто ихсодник
README.pdf:

###
## чистка
######

clean:
	rm -v tmp.*.*
