��    O      �  k         �  9   �  -   �  ,   !  8   N  3   �  0   �  *   �  N     /   f  N   �     �  *   	  +   0	     \	  !   x	  +   �	  )   �	  #   �	  &   
  -   ;
  !   i
  !   �
  +   �
  "   �
  (   �
     %  S   :  #   �  #   �  #   �  #   �  #     #   B  \   f  +   �  0   �         @   A  D   �  &   �  -   �       )   ,  )   V  )   �  )   �  )   �  )   �  )   (  )   R  )   |  )   �     �  V   �  )   D  )   n  )   �  ,   �  )   �  )     )   C  )   m  )   �  )   �  )   �  )     	   ?  �   I     �  &     !   (  )   J  -   t     �     �     �     �  )   �  �    C   �  0   �  9     L   K  E   �  F   �  9   %  n   _  >   �  p     *   ~  9   �  9   �       3   <  0   p  1   �  ,   �  .      8   /  +   h  *   �  .   �  1   �  2         S  ]   k  ,   �  ,   �  ,   #  ,   P  ,   }  ,   �  x   �  5   P  :   �  (   �  L   �  O   7  0   �  ;   �     �  5     4   =  7   r  5   �  4   �  4      5   J   5   �   5   �   5   �   !   "!  g   D!  5   �!  5   �!  5   "  8   N"  5   �"  5   �"  5   �"  5   )#  7   _#  5   �#  5   �#  5   $  
   9$  �   D$  &   %  0   3%      d%  5   �%  4   �%     �%  	   �%     	&     $&  6   =&        5       $       +           -      @   *      G                  <   A   6      M   '           N   /          H   8               L   1          :             F      	   C       &                  D   ;   0               !      ,         O      K      B             =      #   %   9   4          2         )   ?       
       J   7              (   .               "   I       3      E   >    
If these values seem acceptable, use -f to force reset.
 
Report bugs to <pgsql-bugs@postgresql.org>.
   --help          show this help, then exit
   --version       output version information, then exit
   -O OFFSET       set next multitransaction offset
   -e XIDEPOCH     set next transaction ID epoch
   -f              force update to be done
   -l TLI,FILE,SEG force minimum WAL starting location for new transaction log
   -m XID          set next multitransaction ID
   -n              no update, just show extracted control values (for testing)
   -o OID          set next OID
   -x XID          set next transaction ID
 %s resets the PostgreSQL transaction log.

 %s: OID (-o) must not be 0
 %s: cannot be executed by "root"
 %s: could not change directory to "%s": %s
 %s: could not create pg_control file: %s
 %s: could not delete file "%s": %s
 %s: could not open directory "%s": %s
 %s: could not open file "%s" for reading: %s
 %s: could not open file "%s": %s
 %s: could not read file "%s": %s
 %s: could not read from directory "%s": %s
 %s: could not write file "%s": %s
 %s: could not write pg_control file: %s
 %s: fsync error: %s
 %s: internal error -- sizeof(ControlFileData) is too large ... fix PG_CONTROL_SIZE
 %s: invalid argument for option -O
 %s: invalid argument for option -e
 %s: invalid argument for option -l
 %s: invalid argument for option -m
 %s: invalid argument for option -o
 %s: invalid argument for option -x
 %s: lock file "%s" exists
Is a server running?  If not, delete the lock file and try again.
 %s: multitransaction ID (-m) must not be 0
 %s: multitransaction offset (-O) must not be -1
 %s: no data directory specified
 %s: pg_control exists but has invalid CRC; proceed with caution
 %s: pg_control exists but is broken or unknown version; ignoring it
 %s: transaction ID (-x) must not be 0
 %s: transaction ID epoch (-e) must not be -1
 64-bit integers Blocks per segment of large relation: %u
 Bytes per WAL segment:                %u
 Catalog version number:               %u
 Database block size:                  %u
 Database system identifier:           %s
 Date/time type storage:               %s
 First log file ID after reset:        %u
 First log file segment after reset:   %u
 Float4 argument passing:              %s
 Float8 argument passing:              %s
 Guessed pg_control values:

 If you are sure the data directory path is correct, execute
  touch %s
and try again.
 Latest checkpoint's NextMultiOffset:  %u
 Latest checkpoint's NextMultiXactId:  %u
 Latest checkpoint's NextOID:          %u
 Latest checkpoint's NextXID:          %u/%u
 Latest checkpoint's TimeLineID:       %u
 Latest checkpoint's oldestActiveXID:  %u
 Latest checkpoint's oldestXID's DB:   %u
 Latest checkpoint's oldestXID:        %u
 Maximum columns in an index:          %u
 Maximum data alignment:               %u
 Maximum length of identifiers:        %u
 Maximum size of a TOAST chunk:        %u
 Options:
 The database server was not shut down cleanly.
Resetting the transaction log might cause data to be lost.
If you want to proceed anyway, use -f to force reset.
 Transaction log reset
 Try "%s --help" for more information.
 Usage:
  %s [OPTION]... DATADIR

 WAL block size:                       %u
 You must run %s as the PostgreSQL superuser.
 by reference by value floating-point numbers pg_control values:

 pg_control version number:            %u
 Project-Id-Version: pg_resetxlog (PostgreSQL 9.1)
Report-Msgid-Bugs-To: pgsql-bugs@postgresql.org
POT-Creation-Date: 2013-01-29 13:57+0000
PO-Revision-Date: 2012-02-21 22:53-0300
Last-Translator: Álvaro Herrera <alvherre@alvh.no-ip.org>
Language-Team: Español <pgsql-es-ayuda@postgresql.org>
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
Si estos valores parecen aceptables, use -f para forzar reinicio.
 
Reporte errores a <pgsql-bugs@postgresql.org>.
   --help          muestra esta ayuda y sale del programa
   --version       despliega la información de versión y sale del programa
   -O OFFSET       asigna la siguiente posición de multitransacción
   -e XIDEPOCH     asigna el siguiente «epoch» de ID de transacción
   -f              fuerza que la actualización sea hecha
   -l TLI,FILE,SEG fuerza una posición mínima de inicio de WAL para una
                  nueva transacción
   -m XID          asigna el siguiente ID de multitransacción
   -n              no actualiza, sólo muestra los valores de control extraídos
                  (para prueba)
   -o OID          asigna el siguiente OID
   -x XID          asigna el siguiente ID de transacción
 %s reinicia la bitácora de transacciones de PostgreSQL

 %s: OID (-o) no debe ser cero
 %s: no puede ser ejecutado con el usuario «root»
 %s: no se pudo cambiar al directorio «%s»: %s
 %s: no se pudo crear el archivo pg_control:   %s
 %s: no se pudo borrar el archivo «%s»: %s
 %s: no se pudo abrir el directorio «%s»: %s
 %s: no se pudo abrir el archivo «%s» para lectura: %s
 %s: no se pudo abrir el archivo «%s»: %s
 %s: no se pudo leer el archivo «%s»: %s
 %s: no se pudo leer del directorio «%s»: %s
 %s: no se pudo escribir en el archivo «%s»: %s
 %s: no se pudo escribir el archivo pg_control: %s
 %s: Error de fsync: %s
 %s: error interno -- sizeof(ControlFileData) es demasiado grande ... corrija PG_CONTROL_SIZE
 %s: argumento no válido para la opción -O
 %s: argumento no válido para la opción -e
 %s: argumento no válido para la opción -l
 %s: argumento no válido para la opción -m
 %s: argumento no válido para la opción -o
 %s: argumento no válido para la opción -x
 %s: el archivo candado «%s» existe
¿Hay un servidor corriendo? Si no, borre el archivo candado e inténtelo de nuevo
 %s: el ID de multitransacción (-m) no debe ser cero
 %s: la posición de multitransacción (-O) no debe ser -1
 %s: directorio de datos no especificado
 %s: existe pg_control pero tiene un CRC no válido, proceda con precaución
 %s: existe pg_control pero está roto o se desconoce su versión; ignorándolo
 %s: el ID de transacción (-x) no debe ser cero
 %s: el «epoch» de ID de transacción (-e) no debe ser -1
 enteros de 64 bits Bloques por segmento de relación grande:         %u
 Bytes por segmento WAL:                          %u
 Número de versión de catálogo:                   %u
 Tamaño del bloque de la base de datos:           %u
 Identificador de sistema:                        %s
 Tipo de almacenamiento hora/fecha:               %s
 Primer ID de archivo log después de reset:       %u
 Primer segmento de archivo log después de reset: %u
 Paso de parámetros float4:                       %s
 Paso de parámetros float8:                       %s
 Valores de pg_control asumidos:

 Si está seguro que la ruta al directorio de datos es correcta, ejecute
   touch %s
y pruebe de nuevo.
 NextMultiOffset del checkpoint más reciente:     %u
 NextMultiXactId del checkpoint más reciente:     %u
 NextOID del checkpoint más reciente:             %u
 NextXID del checkpoint más reciente:             %u/%u
 TimeLineID del checkpoint más reciente:          %u
 oldestActiveXID del checkpoint más reciente:     %u
 BD del oldestXID del checkpoint más reciente:    %u
 oldestXID del checkpoint más reciente:           %u
 Máximo número de columnas en un índice:          %u
 Máximo alineamiento de datos:                    %u
 Longitud máxima de identificadores:              %u
 Longitud máxima de un trozo TOAST:               %u
 Opciones:
 El servidor de base de datos no fue terminado limpiamente.
Reiniciar la bitácora de transacciones puede causar pérdida de datos.
Si de todas formas quiere proceder, use -f para forzar su reinicio.
 Bitácora de transacciones reiniciada
 Prueba con «%s --help» para más información
 Uso:
   %s [OPCION]... DATADIR

 Tamaño del bloque de WAL:                        %u
 Debe ejecutar %s con el superusuario de PostgreSQL.
 por referencia por valor números de punto flotante Valores de pg_control:

 Número de versión de pg_control:                 %u
 