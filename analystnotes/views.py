from serializers import CommandSerializer, ProjectSerializer
from models import Project, Command
from rest_framework import viewsets, routers
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from permissions import ObjectOwnerPermission, ProjectOwnerPermission
from filters import ObjectOwnerFieldPermissionsFilter


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions, ObjectOwnerPermission)
    filter_backends = (ObjectOwnerFieldPermissionsFilter, )

    def perform_create(self, serializer):
        print "saving as %s" % self.request.user
        serializer.save(owner=self.request.user)


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions, ProjectOwnerPermission)


router = routers.DefaultRouter()
router.register(r'cmd', CommandViewSet)
router.register(r'project', ProjectViewSet)