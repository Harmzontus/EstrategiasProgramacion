public class MayorityElement {
    public static void main(String[] args) {
        int[] arreglo = {5, 5, 1, 1, 1, 5, 5, 5};
        int resultado = elementoMayoritarioRec(arreglo, 0, arreglo.length -1);
        System.out.println("Elemento mayoritario: " + resultado);
    }

    // Primer entrada: {5, 5, 1, 1, 1, 5, 5}, 0, 7
    private static int elementoMayoritarioRec(int[] numeros, int izquierda, int derecha ) {
        // Caso base: un solo elemento
        if (izquierda == derecha ) {
            return numeros[izquierda];
        }

        int mitad = (izquierda + derecha)/2;

        int mayorIzquierda = elementoMayoritarioRec(numeros, izquierda, mitad);
        int mayorDerecha = elementoMayoritarioRec(numeros, mitad + 1, derecha);
        
        if(mayorIzquierda == mayorDerecha) {
            return mayorIzquierda;
        }
        
        int contadorIzquierda = contador(numeros, mayorIzquierda, izquierda, derecha);
        int contadorDerecha = contador(numeros, mayorDerecha, izquierda, derecha);
        
        int rangoMayoria = (derecha - izquierda + 1) / 2;
        
        if (contadorIzquierda > rangoMayoria) return mayorIzquierda;
        if (contadorDerecha > rangoMayoria) return mayorDerecha;
        
        return -1;
    }

    private static int contador(int[] numeros, int numero, int izquierda, int derecha) {
        int contador = 0;
        for (int i = izquierda; i <= derecha; i++) {
            if(numeros[i] == numero) {
                contador ++; 
            }
        }
        return contador;
    }

}