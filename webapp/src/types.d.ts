export interface IRoomPhotoPhoto {
  id: string;
  file: string;
  description: string;
}

export interface IRoomList {
  id: number;
  name: string;
  country: string;
  city: string;
  price: number;
  rating: number;
  is_owner: boolean;
  photos: IRoomPhotoPhoto[];
}

export interface IRoomOwner {
  email: string;
  username: string;
  first_name: string;
  last_name: string;
}

export interface IAmenity {
  name: string;
  description: string;
}

export interface IRoomDetail extends IRoomList {
  created_at: string;
  updated_at: string;
  rooms: number;
  toilets: number;
  description: string;
  address: string;
  pet_friendly: true;
  kind: string;
  is_owner: boolean;
  is_liked: boolean;
  category: {
    name: string;
    kind: string;
  };
  owner: IRoomOwner;
  amenities: IAmenity[];
}

interface result {
  id: number;
  created_at: string;
  updated_at: string;
  payload: string;
  rating: number;
  user: IRoomOwner;
}

export interface IRoomReview {
  count: number;
  next: string;
  previous: string;
  results: result[];
}

export interface User {
  last_login: string;
  is_superuser: boolean;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  is_staff: boolean;
  is_active: boolean;
  date_joined: string;
  avatar: string;
  gender: string;
  language: string;
  currency: string;
  is_host: boolean;
}
