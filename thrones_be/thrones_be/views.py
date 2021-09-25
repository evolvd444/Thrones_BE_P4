from django.shortcuts import render, redirect
from .models import Bathroom
from django.http import HttpResponse
from .forms import BathroomForm
# from .forms import ArtistForm
# from rest_framework import generics
# from .serializers import ArtistSerializer, SongSerializer
# Create your views here.


def bathrooms(request):
    bathrooms = Bathroom.objects.all()
    context = {'bathrooms': bathrooms}
    return render(request,'thrones_be/thrones.html', context)

def bathroom(request, pk):
    bathroomObj = Bathroom.objects.get(id=pk)
    
    return render(request,'thrones_be/throne.html', {'bathroom': bathroomObj})

def createThrone(request):
    form = BathroomForm()
    if request.method == 'POST':
        form = BathroomForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('bathrooms')

    context = {'form': form}
    return render(request,'thrones_be/thrones_list.html', context)


def updateThrone(request, pk):
    bathroom = Bathroom.objects.get(id=pk)
    form = BathroomForm(instance=bathroom)

    if request.method == 'POST':
        form = BathroomForm(request.POST, instance=bathroom)
        if form.is_valid():
             form.save()
             return redirect('bathrooms')

    context = {'form': form}
    return render(request,'thrones_be/thrones_list.html', context)

def deleteThrone(request, pk):
        bathroom = Bathroom.objects.get(id=pk)
        if request.method == 'POST':
            bathroom.delete()
            return redirect('bathrooms')

        context = {'object': bathroom}
        return render(request, 'thrones_be/delete_obj.html', context)


#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')

# def demo_json(request):
#     data = {'a':1, 'b': True}
#     return JsonResponse(data, safe=False)

# def artist_json(request):
#     artists = Artist.objects.all('name', 'nationality', 'photo_url')
#     artist_list = list(artists)
#     return JsonResponse(artist_list, safe=False)



# def artist_list(request):
   
#     artists = Artist.objects.all()
#     artists = artists.order_by('name')
   
#     # artists = list(artists)
#     # artists.sort(lambda e: e[1])

#     print(artists)

#     return render(
#             request, 
#             'tunr/artist_list.html', 
#             {'artists':artists},
#             )


# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#         else:
#             form = ArtistForm()
#     else:
#         form = ArtistForm()
#     return render(request, 'tunr/artist_form.html', {'form':form})


# def artist_edit(request, pk):
#     artist = Artist.objects.get(pk=pk) # Todo.findById(req.params.id)
#     if request.method == "POST":
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'tunr/artist_form.html', {'form': form})

# def artist_delete(request, pk):
#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')


# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'tunr/song_list.html', {'songs': songs})

# def song_detail(request, pk):
#     song = Song.objects.get(id=pk)
#     return render(request, 'tunr/song_detail.html', {'song': song})

# def artist_detail(request, pk):
    
#     try:
#         artist = Artist.objects.get(id=pk)
#     except:
#         artist = {
#             'name': "No artist found", 
#             'nationality': f'with id {pk}'
#             }
#         print(f"artist with id={pk} didn't work")
    
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})


# class BathroomList(generics.ListCreateAPIView):
#     queryset = Bathroom.objects.all()
#     serializer_class = ArtistSerializer

# class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# class SongList(generics.ListCreateAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer

# class SongDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer 