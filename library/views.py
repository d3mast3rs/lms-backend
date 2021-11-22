from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, BookSerializer, AuthorSerializer, UserLoginSerializer, GenreSerializer, PublisherSerializer, LibraryCardSerializer
from .models import User, Book, Author, Genre, Publisher, LibraryCard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET'])
def apiOverview(request):
    return Response("API BASE POINT")




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
  
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        l_serializer = LibraryCardSerializer(data = {"user_id": serializer.data["id"], "first_name": serializer.data["first_name"], "last_name": serializer.data["last_name"]})
        if l_serializer.is_valid():
            l_serializer.save()

    return Response({"data": serializer.data, "message": "Your library card has been issued."})

# userLogin
class TokenObtainPairViewSelf(TokenObtainPairView):
    serializer_class = UserLoginSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=404, data = {"message": "User with the given ID does not exist."})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userUpdate(request, pk):
    try: 
        user = User.objects.get(pk=pk)
        print(user, request.data)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=404, data = {"message": "User with the given ID does not exist."})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userDelete(request, pk):
    try: 
        user = User.objects.get(pk=pk)
        user.delete()

        return Response(f'User with the given ID has been deleted.')
    except User.DoesNotExist:
        return Response(status=404, data = {"message": "User with the given ID does not exist."})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookDetail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=404, data = {"message": "Book with the given ID does not exist."})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def bookUpdate(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if "users_who_issued" in request.data.keys():
                for i in request.data["users_who_issued"]:
                    book.num_of_issued = book.num_of_issued + 1
                    book.num_of_available = book.num_of_available - 1
                    book.save()

        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=404, data = {"message": "Book with the given ID does not exist."})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def bookDelete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response("Book has been deleted.")
    except Book.DoesNotExist:
        return Response(status=404, data = {"message": "Book with the given ID does not exist."})




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def authorCreate(request):
    serializer = AuthorSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authorList(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genreCreate(request):
    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genreList(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publisherCreate(request):
    serializer = PublisherSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def publisherList(request):
    publishers = Publisher.objects.all()
    serializer = PublisherSerializer(publishers, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libraryCardDetail(request, pk):
    try:
        libraryCard = LibraryCard.objects.get(pk=pk)
        serializer = LibraryCardSerializer(libraryCard)
        return Response(serializer.data)
    except LibraryCard.DoesNotExist:
        return Response(status=404, data = {"message": "Library card does not exist."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libraryCardList(request):
    library_cards = LibraryCard.objects.all()
    serializer = LibraryCardSerializer(library_cards, many=True)
    return Response(serializer.data)