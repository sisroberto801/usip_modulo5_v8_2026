class TasksAPI {
    constructor() {
        this.baseURL = '/proyecto';
    }

    request = async (endpoint, options = {}) => {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`Error en API call a ${endpoint}:`, error);
            throw error;
        }
    }

    getStatistics = async () => this.request('/tareas-estadisticas/')

    getPeople = async () => this.request('/personas')

    getTasksByPerson = async (personId) => this.request(`/personas/${personId}/tareas/`)

    getAllTasks = async () => {
        try {
            console.log('Getting all tasks from /todas-tareas/');
            const data = await this.request('/todas-tareas/');
            console.log('All tasks response:', data);
            
            // Transform the data to match the expected format
            const transformedTasks = data.tareas_asignadas.map(task => ({
                ...task,
                person_name: `${task.persona.nombre} ${task.persona.apellido}`,
                person_id: task.persona.id
            }));
            
            console.log('Transformed tasks:', transformedTasks);
            return transformedTasks;
        } catch (error) {
            console.error('Error getting all tasks:', error);
            throw error;
        }
    }
}

const tasksAPI = new TasksAPI();
