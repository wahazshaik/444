export const hasPermission = (permission, userPermissions = []) => {
  return userPermissions.includes(permission);
};
