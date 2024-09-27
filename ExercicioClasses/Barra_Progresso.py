from tqdm import tqdm

class Barra_Progresso:

    def __init__(self):
        pass

    def definir_barra_progresso(self, progresso_maximo):
        """
        Inicializa e retorna uma barra de progresso.

        Este método utiliza a biblioteca `tqdm` para criar uma barra de progresso com base no valor máximo fornecido. 
        A barra de progresso é usada para monitorar visualmente o progresso de uma operação iterativa.

        Parâmetros
        ----------
        progresso_maximo : int
            O valor máximo que a barra de progresso deve atingir (total de iterações ou operações).

        Retorna
        -------
        tqdm.std.tqdm
            Um objeto `tqdm` que representa a barra de progresso.
        """
        bprogresso = tqdm(total=progresso_maximo, position=0, leave=True)
        return bprogresso

    def update(self, bprogresso):
        """
        Atualiza a barra de progresso em uma unidade.

        Este método avança a barra de progresso fornecida em uma unidade, usando o método `update()` do objeto `tqdm`.

        Parameters
        ----------
        bprogresso : tqdm.std.tqdm
            Um objeto `tqdm` que representa a barra de progresso.
        """
        return bprogresso.update()