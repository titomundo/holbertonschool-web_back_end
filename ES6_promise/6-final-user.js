import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  return Promise.allSettled(promises)
    .then((data) => data.map((i) => {
      const body = i.status === 'rejected' ? i.reason : i.value;
      return {
        status: i.status,
        value: body,
      };
    }));
}
