import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Backend URL

export const sendMessage = async (message: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/`, { message });
    return response.data;
  } catch (error: any) {
    console.error('Error sending message:', error);
    throw error.response?.data || { error: 'Failed to connect to backend' };
  }
};
