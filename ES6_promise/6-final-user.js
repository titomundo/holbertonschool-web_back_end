import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [uploadPhoto(fileName), signUpUser(firstName, lastName)];

  return Promise.allSettled([promises])
    .then((data) => {
      data.map((i) => {
        const value = i.status === 'rejected' ? i.reason : i.value;
        return {
          status: i.status,
          value,
        };
      });
    });
}
