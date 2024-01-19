import enum
class Roles(enum.Enum):
    ADMIN = "admin"
    REGULAR = "user_basic"

class Permissions(enum.Enum):
    WRITE = 'Write'
    READ = 'Read'
    CREATE = 'Create'
    DELETE = 'Delete'
    UPDATE = 'Update'
    UPLOAD = 'Upload'
    DOWNLOAD = 'Download'