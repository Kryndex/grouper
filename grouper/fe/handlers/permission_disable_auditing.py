from grouper.fe.util import GrouperHandler
from grouper.permissions import disable_permission_auditing, NoSuchPermission
from grouper.user_permissions import user_is_permission_admin


class PermissionDisableAuditing(GrouperHandler):
    def post(self, user_id=None, name=None):
        if not user_is_permission_admin(self.session, self.current_user):
            return self.forbidden()

        try:
            disable_permission_auditing(self.session, name, self.current_user.id)
        except NoSuchPermission:
            return self.notfound()

        # No explicit refresh because handler queries SQL.
        return self.redirect("/permissions/{}".format(name))
