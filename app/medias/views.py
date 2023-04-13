from medias.models import (
    Photo,
    Video,
)
from rooms.models import Room
from experiences.models import Experience

# serializer
from medias.serializers import (
    PhotoSerializer,
    VideoSerializer,
)

from rest_framework.viewsets import ModelViewSet


class PhotoViewset(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    # lookup_field = "id"
    # lookup_url_kwarg = "photo_id"

    def perform_create(self, serializer):
        # request.data: <QueryDict: {'file': ['asjkdlf'], 'description': ['1'], 'room': ['1'], 'experience': ['2']}>

        room = Room.objects.get(id=self.request.data.get("room"))
        experience = Experience.objects.get(id=self.request.data.get("experience"))
        serializer.save(
            room=room,
            experience=experience,
        )
