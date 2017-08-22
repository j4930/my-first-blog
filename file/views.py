from django.shortcuts import render
from django.http import HttpResponse

def Form(request):
	return render(request, 'file/form.html',{})

def Upload(request):
	if request.method == 'POST':
		if 'file' in request.FILES:
			file = request.FILES['file']
			filename = file.name

			fp = open('%s/%s' % ('/Users/jeonjongmin/mysite/upload/media',filename) ,'wb')
			for chunk in file.chunks():
				fp.write(chunk)
			fp.close()
			return HttpResponse("파일이 업로드되었습니다.")
	return HttpResponse("파일업로드가 실패하였습니다")